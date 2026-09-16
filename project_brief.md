# My agent: AATIA (Asset & Travel Insurance Agent)

One-liner: A conversational banking agent that helps bank customers manage asset and travel insurance policies, file claim receipts, and receive automated payout decisions.

## Insurance Coverage Lines:
1. **Travel & Mobility**: Flight delays, lost baggage, overseas emergency medical, travel theft, rental CDW excess.
2. **Personal & Business Assets**: Mobile gadgets/electronics, auto mobility, home property, commercial inventory & equipment, fine art & luxury assets.
3. **Specialized Protection**: Cyber risk, business interruption, health/accident, key-person loan protection.

## Tool coverage:
- **Memory**: User/business profile, active policies across travel and assets, claim history, preferred payout bank accounts, deductible balances.
- **Tools**: Policy catalog & terms lookup, receipt/invoice document parser, merchant & Tax ID verification, fraud risk scoring, instant claim payout execution.
- **Catalog/UI**: Travel & asset policy catalog cards, claims progress tracker timeline, deductible/co-pay summary tables, fraud risk alert cards.
- **Image gen**: Visual policy coverage infocards and receipt claim summary graphics.
- **Sandbox**: Actuarial payout math ($\text{Payout} = [\text{Expense} - \text{Deductible}] \times \text{Co-pay Rate}$), business interruption loss calculations, multi-currency FX conversions.

## Architecture & Integration:
- **Core rails**: Memory, function tools, evaluation dataset, Agent Runtime deployment, FastAPI Cloud Run frontend.
- **Stretch menu**: A2UI display cards, RAG multi-policy handbook search, vision AI receipt forensics, code sandbox payout math, automated fraud guardrails.

## First eval questions:
- **Travel Claim**: "I paid $850 for an emergency dental treatment while on vacation in London. My travel policy deductible is $100 with 80% coverage. What is my payout?"
- **Asset Claim**: "My laptop screen cracked while working at a coffee shop. The repair quote is $400. My gadget policy has a $50 deductible and 80% coverage. How much will AATIA reimburse?"
