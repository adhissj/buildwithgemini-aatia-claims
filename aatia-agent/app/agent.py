# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import random
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types


# Mock Bank Customer Database for Validation
BANK_CUSTOMERS = {
    "USR-101": {"name": "Alice Johnson", "phone": "+1-555-0199", "email": "alice@example.com", "account": "Checking (***4321)", "status": "ACTIVE_VERIFIED", "kyc": "PASSED"},
    "USR-102": {"name": "Bob Smith", "phone": "+1-555-0288", "email": "bob@example.com", "account": "Savings (***8765)", "status": "ACTIVE_VERIFIED", "kyc": "PASSED"},
    "SME-500": {"name": "Artisan Bakery LLC", "phone": "+1-555-0900", "email": "info@artisanbakery.com", "account": "Business Checking (***9988)", "status": "ACTIVE_VERIFIED", "kyc": "PASSED"},
}


def verify_otp(phone_or_email: str, otp_code: str = "123456") -> str:
    """Verifies customer One-Time Password (OTP) sent via SMS or Email for quick secure authentication.

    Args:
        phone_or_email: Customer phone number (e.g. '+1-555-0199') or email address (e.g. 'alice@example.com').
        otp_code: 6-digit OTP verification code entered by user.

    Returns:
        OTP verification result string with customer name and authentication token.
    """
    target = phone_or_email.strip().lower()
    found_name = "Alice Johnson"
    found_id = "USR-101"

    for cid, info in BANK_CUSTOMERS.items():
        if target in info["phone"] or target in info["email"].lower():
            found_name = info["name"]
            found_id = cid
            break

    return (
        f"🔐 **OTP Authentication SUCCESSFUL**:\n"
        f"• Verified Identity: {phone_or_email}\n"
        f"• Customer Name: **{found_name}** (`{found_id}`)\n"
        f"• Auth Status: **VERIFIED_SECURE**\n"
        f"• Action: Customer authenticated. Display welcome message and proceed to claim category selection."
    )


def validate_bank_account(customer_id_or_name: str) -> str:
    """Validates customer identity, bank account standing, and KYC verification status with the bank core.

    Args:
        customer_id_or_name: Customer ID (e.g. 'USR-101') or Customer Name (e.g. 'Alice Johnson').

    Returns:
        Validation status report string including account standing, account holder name, and target payout account.
    """
    query = customer_id_or_name.strip().upper()
    for cid, info in BANK_CUSTOMERS.items():
        if query in cid or query in info["name"].upper():
            return (
                f"🏦 **Bank Account Validation SUCCESS**:\n"
                f"• Customer ID: `{cid}`\n"
                f"• Account Holder: {info['name']}\n"
                f"• Verified Account: {info['account']}\n"
                f"• Account Standing: **{info['status']}**\n"
                f"• KYC Compliance Status: **{info['kyc']}**"
            )

    return (
        f"🏦 **Bank Account Validation SUCCESS**:\n"
        f"• Customer Query: `{customer_id_or_name}`\n"
        f"• Verified Account: Checking (***1234)\n"
        f"• Account Standing: **ACTIVE_VERIFIED**\n"
        f"• KYC Compliance Status: **PASSED (Verified Bank Client)**"
    )


def list_policy_categories_and_products() -> str:
    """Lists all available insurance categories and products supported by AATIA, including option for custom product entry.

    Returns:
        Structured list of insurance categories and products.
    """
    return (
        "🌐 **AATIA Insurance Categories & Products (* Required)**:\n\n"
        "1. **Retail & Lifestyle Lines**:\n"
        "   • `travel`: Travel & Mobility (Medical, Baggage, Flight Delay, CDW)\n"
        "   • `gadget`: Mobile Devices & Electronics (Phones, Laptops, Tablets)\n"
        "   • `auto`: Auto Mobility & Excess Reimbursement\n"
        "   • `health`: Outpatient Health & Prescription Reimbursement\n"
        "   • `home`: Home Contents & Mortgage Unemployment Protection\n\n"
        "2. **Commercial & SME Lines**:\n"
        "   • `spoilage`: Commercial Property & Inventory Spoilage\n"
        "   • `business_interruption`: Business Revenue Interruption\n"
        "   • `cyber`: Cyber Risk, Ransomware & Data Breach\n"
        "   • `workers_comp`: Employer Liability & Workplace Injury\n\n"
        "3. **Private Banking & HNW Lines**:\n"
        "   • `luxury`: Fine Art, Luxury Watches & Collectibles\n"
        "   • `marine_aviation`: Marine Yacht & Private Aviation Hull Protection\n\n"
        "✍️ *Note: If your product is not listed above, type your custom product name (e.g. 'Electric Scooter Protection', 'Drone Camera Insurance').*"
    )


def get_policy_document_package(category: str, product_name: str) -> str:
    """Retrieves the official policy document package, terms, exclusions, and mandatory claim document requirements for a selected category and product.

    Args:
        category: Category name (e.g. 'Retail', 'Commercial', 'Private Banking').
        product_name: Product name (e.g. 'travel', 'gadget', 'spoilage', 'auto', 'health', 'home', or custom product).

    Returns:
        Full policy document package text with terms, coverage limits, sub-limits, exclusions, and mandatory document checklist.
    """
    p = product_name.lower()
    if "travel" in p:
        return (
            "📄 **OFFICIAL POLICY DOCUMENT: Travel & Mobility Protection (Ref: POL-TRV-2026)**\n"
            "• **Category**: Retail & Lifestyle Insurance\n"
            "• **Coverage Terms**: Emergency medical clinics, trip delays (> 6h), lost baggage, stolen items.\n"
            "• **Deductible**: $100 flat deductible per incident.\n"
            "• **Coverage Rate**: 80% after deductible for medical / 100% for baggage & flight delay stipend.\n"
            "• **Max Policy Cap**: $50,000 per trip.\n"
            "• **Sub-Limits**: Emergency Dental max $1,000; Stolen Item max $250/item.\n"
            "• **Explicit Exclusions**: Un-declared pre-existing conditions, extreme sports without rider, unattended luggage in public.\n"
            "• **Mandatory Claim Documents (* Mandatory)**:\n"
            "  1. Boarding Pass / Travel Itinerary\n"
            "  2. Itemized Clinic / Hotel / Airline Invoice\n"
            "  3. Police Theft Report (if stolen, filed within 24h) or Airline PIR (for baggage delay)."
        )
    elif "gadget" in p or "phone" in p or "device" in p or "laptop" in p:
        return (
            "📄 **OFFICIAL POLICY DOCUMENT: Mobile Device & Electronics Protection (Ref: POL-GDT-2026)**\n"
            "• **Category**: Retail & Lifestyle Insurance\n"
            "• **Coverage Terms**: Accidental screen cracks, back glass breakage, liquid spills, forced entry theft.\n"
            "• **Deductible & Co-Pay**: $50 minimum deductible; 20% co-pay (80% coverage rate).\n"
            "• **Max Policy Cap**: $2,500 per device; max 2 claims per 12 months.\n"
            "• **Explicit Exclusions**: Cosmetic scratches, battery degradation, mysterious disappearance, jailbroken software.\n"
            "• **Mandatory Claim Documents (* Mandatory)**:\n"
            "  1. Itemized Repair Shop Invoice / Receipt\n"
            "  2. Photo of Device IMEI / Serial Number\n"
            "  3. Carrier IMEI Blacklist Notice (for theft claims)."
        )
    elif "spoilage" in p or "commercial" in p or "sme" in p:
        return (
            "📄 **OFFICIAL POLICY DOCUMENT: SME Inventory & Stock Spoilage (Ref: POL-SME-2026)**\n"
            "• **Category**: Commercial & SME Insurance\n"
            "• **Coverage Terms**: Perishable raw materials, food inventory, or pharmaceutical stock lost to power outages > 4 hours.\n"
            "• **Deductible & Coverage**: $500 deductible; 90% reimbursement coverage rate.\n"
            "• **Max Policy Cap**: $100,000 per location.\n"
            "• **Explicit Exclusions**: Employee theft/embezzlement, routine maintenance failure, unrecorded inventory shrinkage.\n"
            "• **Mandatory Claim Documents (* Mandatory)**:\n"
            "  1. POS Inventory Valuation Ledger\n"
            "  2. Cold Storage Temperature Sensor Log\n"
            "  3. Utility Power Outage Notice."
        )
    else:
        return (
            f"📄 **OFFICIAL POLICY DOCUMENT: {product_name.upper()} ({category.upper()})**\n"
            "• **Coverage Terms**: Comprehensive asset protection under master bancassurance agreement.\n"
            "• **Deductible**: $100 standard deductible.\n"
            "• **Coverage Rate**: 80% reimbursement after deductible.\n"
            "• **Mandatory Claim Documents (* Mandatory)**:\n"
            "  1. Itemized Repair/Purchase Receipt\n"
            "  2. Proof of Payment / Bank Statement\n"
            "  3. Brief Incident Description & Incident Photos."
        )


def calculate_claim_payout(expense_amount: float, deductible: float = 100.0, coverage_rate: float = 0.80) -> str:
    """Calculates the net claim reimbursement payout after applying deductibles and co-pay coverage rates.

    Args:
        expense_amount: The total expense or loss claimed in USD.
        deductible: The policy deductible amount in USD (default $100).
        coverage_rate: The policy coverage percentage rate decimal between 0.0 and 1.0 (default 0.80 for 80%).

    Returns:
        A detailed breakdown of the deductible calculation and net payout amount.
    """
    if expense_amount <= deductible:
        return (
            f"🧮 **Payout Calculation Breakdown**:\n"
            f"• Claimed Expense: ${expense_amount:.2f}\n"
            f"• Policy Deductible: ${deductible:.2f}\n"
            f"• Net Payout: $0.00 (Expense is below policy deductible)."
        )

    covered_base = expense_amount - deductible
    net_payout = covered_base * coverage_rate

    return (
        f"🧮 **Payout Calculation Breakdown**:\n"
        f"• Total Claimed Expense: ${expense_amount:.2f}\n"
        f"• Less Deductible: -${deductible:.2f}\n"
        f"• Eligible Amount: ${covered_base:.2f}\n"
        f"• Coverage Rate: {coverage_rate * 100:.0f}%\n"
        f"• **Approved Net Payout**: **${net_payout:.2f}**"
    )


PROCESSED_CLAIMS_LEDGER = set()


def check_fraud_risk(merchant_name: str, expense_amount: float, receipt_date: str, user_name: str = "Customer") -> str:
    """Performs forensic verification and fraud risk scoring on claim receipt details.

    Args:
        merchant_name: Name of the vendor, hospital, repair shop, or airline.
        expense_amount: The claim total amount in USD.
        receipt_date: The date listed on the receipt (YYYY-MM-DD).
        user_name: Customer name submitting the claim.

    Returns:
        A fraud risk assessment report string with risk score and approval recommendation.
    """
    # Create unique claim invoice fingerprint
    invoice_key = f"{user_name.lower().strip()}:{merchant_name.lower().strip()}:{expense_amount:.2f}:{receipt_date.strip()}"

    if invoice_key in PROCESSED_CLAIMS_LEDGER:
        return (
            f"🚫 **DUPLICATE CLAIM DENIED - HIGH FRAUD RISK** (Score: 99/100)\n"
            f"• Forensic Check: An identical claim receipt ({merchant_name}, ${expense_amount:.2f}, {receipt_date}) has ALREADY been submitted and reimbursed for this customer.\n"
            f"• Action: **CLAIM REJECTED**. Duplicate submissions are flagged under anti-fraud compliance rules."
        )

    risk_score = random.randint(3, 12)
    if expense_amount > 5000:
        risk_score += 25

    if risk_score < 15:
        return (
            f"🛡️ **Fraud Risk Assessment**: LOW RISK (Score: {risk_score}/100)\n"
            f"• Merchant Verification: '{merchant_name}' verified in official business registry.\n"
            f"• Forensic Check: Invoice font alignment clean, date '{receipt_date}' within policy window. No prior duplicate found.\n"
            f"• Recommendation: Approved for **Straight-Through Processing (STP)** instant payout."
        )
    else:
        return (
            f"🛡️ **Fraud Risk Assessment**: ESCALATED FOR REVIEW (Score: {risk_score}/100)\n"
            f"• Merchant Verification: High claim value (${expense_amount:.2f}) requires human audit.\n"
            f"• Recommendation: Routed to Human-In-The-Loop (HITL) Claims Adjuster review."
        )


def submit_claim_payout(user_name: str, product_name: str, approved_payout: float, bank_account: str = "Checking (***1234)", merchant_name: str = "", expense_amount: float = 0.0, receipt_date: str = "") -> str:
    """Executes instant direct deposit disbursement of approved claim payouts into the customer's validated bank account.

    Args:
        user_name: Name of the bank customer.
        product_name: The insurance product name (e.g. 'travel', 'gadget').
        approved_payout: The final approved net payout amount in USD.
        bank_account: Target bank account descriptor (default 'Checking (***1234)').
        merchant_name: Merchant/Vendor name.
        expense_amount: Original claimed amount.
        receipt_date: Date of receipt.

    Returns:
        A confirmation string with claim reference ID and transaction status.
    """
    invoice_key = f"{user_name.lower().strip()}:{merchant_name.lower().strip()}:{expense_amount:.2f}:{receipt_date.strip()}"
    
    if invoice_key in PROCESSED_CLAIMS_LEDGER and approved_payout > 0:
        return (
            "🚫 **CLAIM SUBMISSION BLOCKED**: This invoice has already been paid out previously. "
            "Re-submitting duplicate receipts is strictly prohibited."
        )

    # Store in ledger to prevent double-dipping
    PROCESSED_CLAIMS_LEDGER.add(invoice_key)

    claim_id = f"CLM-2026-{random.randint(10000, 99999)}"
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return (
        f"✅ **Claim Payout Successfully Executed!**\n"
        f"• Claim Reference ID: `{claim_id}`\n"
        f"• Beneficiary: {user_name}\n"
        f"• Insurance Product: {product_name.capitalize()}\n"
        f"• Disbursed Payout: **${approved_payout:.2f}**\n"
        f"• Validated Bank Account: {bank_account}\n"
        f"• Timestamp: {now_str}\n"
        f"• Transaction Status: **COMPLETED (Direct Deposit Disbursed)**"
    )


def generate_settlement_certificate(claim_id: str, user_name: str, product_name: str, approved_payout: float) -> str:
    """Generates an official AATIA Digital Settlement Certificate with cryptographic audit verification and QR code string for policyholder tax/audit records.

    Args:
        claim_id: Approved claim reference ID (e.g. 'CLM-2026-84921').
        user_name: Authenticated customer name.
        product_name: Insurance policy product type (e.g. 'Gadget', 'Auto & Mobility').
        approved_payout: Dollar amount disbursed.

    Returns:
        Formatted digital settlement certificate string with cryptographic hash and verification badge.
    """
    import hashlib
    cert_hash = hashlib.sha256(f"{claim_id}:{user_name}:{approved_payout}:{datetime.datetime.now()}".encode()).hexdigest()[:16].upper()
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

    return (
        f"📜 **AATIA DIGITAL CLAIMS SETTLEMENT CERTIFICATE**\n"
        f"──────────────────────────────────────────────\n"
        f"• **Certificate ID**: `CERT-{cert_hash[:8]}`\n"
        f"• **Claim Reference**: `{claim_id}`\n"
        f"• **Policyholder**: {user_name}\n"
        f"• **Coverage Line**: {product_name.capitalize()} Protection\n"
        f"• **Approved Disbursed Amount**: **${approved_payout:.2f}**\n"
        f"• **Settlement Date**: {now_str}\n"
        f"• **Verification Hash**: `SHA256:{cert_hash}`\n"
        f"• **Audit Status**: **VERIFIED_COMPLIANT (FDIC & AATIA Underwriting)**\n"
        f"• **QR Verification Link**: `https://aatia-insurance.com/verify/{cert_hash}`\n"
        f"──────────────────────────────────────────────"
    )


from google.adk.agents.callback_context import CallbackContext
from google.adk.tools.preload_memory_tool import PreloadMemoryTool


async def generate_memories_callback(callback_context: CallbackContext):
    await callback_context.add_session_to_memory()
    return None


root_agent = Agent(
    name="aatia_root_agent",
    model=Gemini(
        model="gemini-flash-latest",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=(
        "You are AATIA (Asset And Travel Insurance Agent), an intelligent AI claims concierge for bank clients.\n\n"
        "You remember customer facts, policy choices, and past claims from previous sessions using Memory Bank.\n\n"
        "Claim Processing Rules:\n"
        "1. If the user message mentions that the user is OTP-verified / authenticated (e.g. 'User Alice Johnson is fully OTP-VERIFIED'), treat identity verification as COMPLETE.\n"
        "2. Do NOT ask for OTP verification again if the user is already authenticated.\n"
        "3. For claim submissions, execute tool calls in sequence:\n"
        "   a. `calculate_claim_payout(expense_amount, deductible, coverage_rate)`\n"
        "   b. `check_fraud_risk(merchant_name, expense_amount, receipt_date, user_name)`\n"
        "   c. If `check_fraud_risk` returns DUPLICATE CLAIM DENIED or Fraud Score >= 90, DO NOT call `submit_claim_payout`. Immediately REJECT the claim and inform the user that duplicate invoice submissions are prohibited.\n"
        "   d. Otherwise, execute `submit_claim_payout(user_name, product_name, approved_payout, bank_account, merchant_name, expense_amount, receipt_date)`.\n"
        "   e. Call `generate_settlement_certificate(claim_id, user_name, product_name, approved_payout)` to provide a official audit certificate.\n"
        "4. Summarize the decision clearly and concisely."
    ),
    tools=[
        PreloadMemoryTool(),
        verify_otp,
        validate_bank_account,
        list_policy_categories_and_products,
        get_policy_document_package,
        calculate_claim_payout,
        check_fraud_risk,
        submit_claim_payout,
        generate_settlement_certificate,
    ],
    after_agent_callback=generate_memories_callback,
)

app = App(
    root_agent=root_agent,
    name="app",
)



