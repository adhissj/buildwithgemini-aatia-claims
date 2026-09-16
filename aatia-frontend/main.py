"""FastAPI proxy for AATIA Agent Runtime deployment.
The browser communicates with this proxy over HTTP/JSON, and the proxy forwards
messages to the AATIA agent on Vertex AI Agent Runtime over A2A.
"""

import os
import uuid

import google.auth
import google.auth.transport.requests
import httpx
from a2a.client import ClientConfig, ClientFactory
from a2a.types import (
    AgentCard,
    Message,
    Role,
    TaskArtifactUpdateEvent,
    TransportProtocol,
)
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

RESOURCE = os.environ.get(
    "AGENT_ENGINE_RESOURCE_NAME",
    os.environ.get(
        "RESOURCE",
        "projects/756778515744/locations/us-east1/reasoningEngines/3841825568844677120",
    ),
)
AGENT_DIRECTORY = os.environ.get("AGENT_DIRECTORY", "app")
LOCATION = RESOURCE.split("/locations/")[1].split("/")[0]

A2A_BASE = (
    f"https://{LOCATION}-aiplatform.googleapis.com/reasoningEngines/v1/"
    f"{RESOURCE}/api/a2a/{AGENT_DIRECTORY}"
)
A2A_CARD_URL = f"{A2A_BASE}/.well-known/agent-card.json"
_A2UI_MIME = "application/json+a2ui"

_creds = None


def _auth_headers() -> dict[str, str]:
    global _creds
    if _creds is None:
        _creds, _ = google.auth.default(
            scopes=["https://www.googleapis.com/auth/cloud-platform"]
        )
    if not _creds.valid:
        _creds.refresh(google.auth.transport.requests.Request())
    return {
        "Authorization": f"Bearer {_creds.token}",
        "Content-Type": "application/json",
    }


app = FastAPI(title="AATIA Agent Chat Proxy")


@app.exception_handler(Exception)
async def _json_errors(request: Request, exc: Exception):
    return JSONResponse(
        status_code=200,
        content={
            "parts": [{"kind": "text", "text": f"Error: {type(exc).__name__}: {exc}"}]
        },
    )


_contexts: dict[str, str] = {}
_card: AgentCard | None = None


async def _get_card(client: httpx.AsyncClient) -> AgentCard:
    global _card
    if _card is None:
        resp = await client.get(A2A_CARD_URL)
        resp.raise_for_status()
        card = AgentCard(**resp.json())
        card.url = A2A_BASE
        _card = card
    return _card


def _extract_parts(parts: list) -> list[dict]:
    out: list[dict] = []
    for p in parts:
        root = getattr(p, "root", p)
        text_val = getattr(root, "text", None)
        data_val = getattr(root, "data", None)
        file_val = getattr(root, "file", None)
        if text_val:
            out.append({"kind": "text", "text": text_val})
        elif data_val is not None:
            meta = getattr(root, "metadata", None) or {}
            mime = meta.get("mimeType") if isinstance(meta, dict) else None
            if mime == _A2UI_MIME:
                out.append({"kind": "a2ui", "data": data_val})
        elif file_val is not None:
            uri = getattr(file_val, "uri", None)
            if uri:
                out.append({"kind": "text", "text": uri})
    return out


PROCESSED_INVOICES = set()


@app.post("/chat")
async def chat(req: Request):
    body = await req.json()
    message = body.get("message", "")
    user_id = body.get("user_id") or "web-user"
    parts: list[dict] = []

    # Duplicate Invoice Protection Check
    if "Process claim submission for product" in message:
        # Extract invoice key signature
        import re
        merchant_match = re.search(r"Merchant:\s*([^,]+)", message)
        amount_match = re.search(r"Expense Amount:\s*\$([0-9\.]+)", message)
        merchant = merchant_match.group(1).strip().lower() if merchant_match else "unknown"
        amount = amount_match.group(1).strip() if amount_match else "0.00"
        
        invoice_signature = f"{user_id.lower().strip()}:{merchant}:{amount}"
        
        if invoice_signature in PROCESSED_INVOICES:
            return JSONResponse({
                "parts": [{
                    "kind": "text",
                    "text": "🚫 **DUPLICATE CLAIM DENIED - HIGH FRAUD RISK**\n\n"
                            "• **Forensic Check**: An identical claim invoice has ALREADY been processed and paid out for this account.\n"
                            "• **Anti-Fraud Action**: **CLAIM REJECTED**. Re-submitting duplicate receipts is strictly prohibited.\n\n"
                            "--- \n"
                            "❓ **Believe this is an error or suspect unauthorized activity?**\n"
                            "If you did not initiate the previous claim or need to appeal this decision:\n"
                            "📞 **Call Claims Dispute Hotline**: `1-800-AATIA-HELP` (1-800-228-4243)\n"
                            "📧 **Email Claims Audit Team**: `disputes@aatia-insurance.com`\n"
                            "🏛️ **Ref ID for Representative**: `DISPUTE-DUPLICATE-" + merchant.upper()[:10] + "`"
                }]
            })
        
        # Record signature in ledger
        PROCESSED_INVOICES.add(invoice_signature)

    async with httpx.AsyncClient(headers=_auth_headers(), timeout=120) as client:
        card = await _get_card(client)
        factory = ClientFactory(
            ClientConfig(
                supported_transports=[
                    TransportProtocol.jsonrpc,
                    TransportProtocol.http_json,
                ],
                httpx_client=client,
            )
        )
        a2a_client = factory.create(card)

        msg = Message(
            message_id=str(uuid.uuid4()),
            role=Role.user,
            parts=[Part(root=TextPart(text=message))],
            context_id=_contexts.get(user_id),
        )

        last_task = None
        got_artifact_update = False
        async for event in a2a_client.send_message(msg):
            if not isinstance(event, tuple):
                continue
            task, update = event
            if task is not None:
                last_task = task
                if getattr(task, "context_id", None):
                    _contexts[user_id] = task.context_id
            if isinstance(update, TaskArtifactUpdateEvent):
                got_artifact_update = True
                parts.extend(_extract_parts(update.artifact.parts))

        if not got_artifact_update and last_task is not None:
            for artifact in getattr(last_task, "artifacts", None) or []:
                parts.extend(_extract_parts(artifact.parts))

    if not parts:
        parts = [{"kind": "text", "text": "(The agent didn't return a reply.)"}]
    return JSONResponse({"parts": parts})


app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
