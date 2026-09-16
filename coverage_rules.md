# Universal Bancassurance Policy Catalog & Coverage Rules

This document outlines the coverage mechanisms, included objects, explicit exclusions, deductible/co-pay rules, master document requirements, and **Straight-Through Processing (STP) vs. Human-In-The-Loop (HITL) Automation Rules** supported by the Universal Bancassurance Concierge agent.

---

## ⚙️ Straight-Through Processing (STP) vs. Human-In-The-Loop (HITL) Matrix

| Product Line | Fully Automated (STP) Threshold | Escalated to Human Review (HITL) Triggers |
|---|---|---|
| **1.1 Travel & Mobility** | Claims $\le \$500$; flight delays, lost baggage, minor clinic visits. | Claims $> \$5,000$; medical evacuations; un-notified police reports; suspicious receipt edits. |
| **1.2 Device Protection** | Claims $\le \$400$; cracked screens, liquid spills with valid IMEI match. | Theft claims without carrier IMEI blacklist confirmation; multiple claims within 30 days. |
| **1.3 Auto Mobility** | Claims $\le \$500$; windshield repair ($0 deductible), towing receipts. | Major collision excess claims $> \$2,500$; disputed police reports; DUI flags. |
| **1.4 Personal Health** | Claims $\le \$300$; routine GP/specialist visits, prescription drugs. | Inpatient hospital stays $> 3$ days; experimental drug treatment claims. |
| **1.5 Home Protection** | Claims $\le \$1,000$; minor burst pipe repairs, appliance contents. | Structural damage $> \$10,000$; involuntary redundancy mortgage claims; flood zone claims. |
| **2.1 Commercial Stock** | Claims $\le \$1,500$; perishable inventory spoilage with sensor log. | Spoilage $> \$10,000$; machinery failure without maintenance log history. |
| **2.2 Business Interruption**| Claims $\le \$2,500$; short term closure with clear utility notice. | Revenue loss claims $> \$25,000$; disputes over audited P&L baseline. |
| **2.3 Cyber Risk** | Claims $\le \$2,000$; basic IT forensic incident response fees. | All Ransomware extortion payouts; data breach liability claims involving $> 1,000$ users. |
| **2.4 Employer Liability** | Claims $\le \$1,000$; minor workplace emergency room visits. | Permanent disability claims; workplace safety lawsuits; disputed injury incidents. |
| **3.1 Fine Art / Luxury** | None (0% STP — HNW assets require human verification). | All claims (100% HITL required for high-value appraisals and vault security audits). |
| **3.2 Marine & Aviation** | None (0% STP — Marine/Aviation assets require surveyor review). | All claims (100% HITL required for vessel/aircraft hull surveyor inspection). |
| **3.3 Key-Person Life** | None (0% STP — Executive debt protection requires legal review). | All claims (100% HITL required for death certificate / board resolution validation). |

---

## 📋 Master Claims Requirements & Document Verification Matrix

| Product Line | Claim Type | Mandatory Documents Required | Validation Criteria / Verification Rules |
|---|---|---|---|
| **1.1 Travel & Mobility** | Overseas Medical | • Itemized Clinic/Hospital Bill<br>• GP/Doctor Diagnosis Summary<br>• Boarding Pass / E-Ticket | • Date of service must fall within trip dates.<br>• Medical treatment must be non-elective. |
| | Baggage Delay / Loss | • Airline Property Irregularity Report (PIR)<br>• Baggage Tag Receipt<br>• Replacement Items Invoices | • Delay must exceed 6 continuous hours.<br>• Receipts required for emergency attire/toiletries. |
| | Theft / Stolen Property | • Police Report (filed within 24h)<br>• Original Purchase Receipts | • Police report must state incident location & time.<br>• Max sub-limit per item applies ($250). |
| **1.2 Device Protection** | Screen / Hardware Damage | • Repair Shop Itemized Invoice<br>• Device IMEI / Serial Number Photo<br>• Proof of Purchase / Bank Statement | • IMEI on repair invoice must match policy.<br>• Repair must be by certified service center. |
| | Theft | • Police Report showing forced entry<br>• Device IMEI Blacklist Notice | • Theft from unattended public area is rejected.<br>• Carrier IMEI blacklist proof required. |
| **1.3 Auto Mobility** | Collision Excess | • Primary Insurer Settlement Letter<br>• Police Accident Report<br>• Body Shop Repair Invoice | • Driver must hold active driver's license.<br>• Primary insurer must have approved claim first. |
| | Windshield Repair | • Auto Glass Shop Invoice<br>• Damage Photo | • $0 deductible applies for repair (vs replacement). |
| **1.4 Personal Health** | Specialist / Pharmacy | • GP Referral Letter<br>• Itemized Pharmacy/Clinic Invoice<br>• Prescription Document | • Referral must precede specialist visit.<br>• Prescription must match diagnosis. |
| **1.5 Home & Mortgage** | Property Damage | • Damage Photos/Videos<br>• Contractor Itemized Estimate<br>• Proof of Home Ownership | • Damage must stem from sudden event (fire/burst pipe), not gradual wear. |
| | Mortgage Unemployment | • Employment Termination Notice<br>• Severance Agreement<br>• Mortgage Statement | • Involuntary redundancy only; voluntary resignation or termination for cause excluded. |
| **2.1 Commercial Stock** | Inventory Spoilage | • POS Inventory Valuation Ledger<br>• Cold Storage Temperature Sensor Log<br>• Power Utility Outage Notice | • Outage must exceed 4 continuous hours.<br>• Temperature log must prove threshold breach. |
| **2.2 Business Interruption**| Revenue Loss | • Prior 12 Months Profit & Loss (P&L)<br>• Payroll Register & Commercial Lease<br>• Fire/Disaster Inspection Report | • 48-hour elimination period applies.<br>• Claim calculated on net profit + fixed cost. |
| **2.3 Cyber Risk** | Data Breach / Ransomware | • Forensic IT Incident Report<br>• Regulatory Authority Notification<br>• Itemized Legal/PR Invoices | • Incident must be logged by certified IT firm.<br>• Sanctions check required prior to ransom payment. |
| **2.4 Employer Liability** | Workplace Injury | • Incident Injury Log & Safety Report<br>• Attending Physician Statement<br>• Employee Payroll Record | • Injury must occur during scope of employment.<br>• OSHA/Workplace authority must be notified. |
| **3.1 Fine Art / Luxury** | Damage / Theft | • Certified Appraisal Report (< 3 yrs)<br>• High-Res Condition Photos<br>• Police Report (if stolen) | • Payout based on pre-agreed appraisal value.<br>• Vault security logs required for high-value items. |
| **3.2 Marine & Aviation** | Hull / Machinery Damage | • Captain/Pilot Logbook<br>• Marine/Aviation Surveyor Loss Report<br>• Maintenance History Log | • Vessel/aircraft must operate within agreed geographical boundaries. |
| **3.3 Key-Person Life** | Debt Protection | • Official Death Certificate / Disability Panel<br>• Corporate Loan Agreement<br>• Board Resolution | • 2-year suicide contestability clause applies.<br>• Payout sent directly to bank loan account. |

---

## Detailed Product Specifications

### 1. Retail & Lifestyle Insurance Lines

#### 1.1 Travel & Mobility Insurance
* **Coverage Mechanism**: Reimburses policyholders for unexpected emergency expenses, trip delays, lost baggage, or cancellation penalties incurred while traveling outside their home jurisdiction.
* **✅ Included Items / Covered Objects**:
  * Emergency medical clinic bills, hospital stays, and prescribed emergency medication.
  * Checked baggage loss, luggage damage, or delay compensation (> 6 hours).
  * Flight cancellation / trip interruption penalties due to illness, severe weather, or airline insolvency.
  * Stolen personal travel items (cameras, passports, travel cash up to sub-limits).
  * Rental car collision damage waiver (CDW) excess.
* **❌ Excluded Items / Objects (Not Covered)**:
  * Pre-existing medical conditions not declared prior to trip departure.
  * High-risk extreme sports (skydiving, unguided backcountry skiing, scuba diving below 30m) unless rider purchased.
  * Unattended luggage left in public spaces without supervision.
  * Travel to countries under official government travel bans or war zones.
* **Mandatory Documents Required**: Flight itinerary/boarding pass, official airline lost luggage report (PIR), itemized hospital/clinic receipts, police theft report (within 24 hours).
* **Validation & Fraud Rules**:
  * Medical service dates must match flight travel dates.
  * Receipts scanned via Vision AI for altered dates or duplicate totals.
* **Deductible & Co-Pay**: $50–$100 flat deductible per claim incident; 100% coverage after deductible up to $50,000 max policy limit.

---

#### 1.2 Mobile Device & Electronics Protection
* **Coverage Mechanism**: Protects personal electronic devices against accidental damage, liquid spills, screen cracks, and theft.
* **✅ Included Items / Covered Objects**:
  * Smartphones, tablets, laptops, smartwatches, wireless earbuds, and e-readers.
  * Accidental screen cracks, back glass breakage, and chassis drop damage.
  * Liquid damage (water/beverage spills, submersion).
  * Theft from locked premises or vehicle with forced entry evidence.
* **❌ Excluded Items / Objects (Not Covered)**:
  * Cosmetic wear and tear (scratches, minor scuffs, paint peeling that do not impair functionality).
  * Battery degradation over time or normal capacity loss.
  * Loss due to mysterious disappearance or forgetting device in public.
  * Unauthorized third-party modifications or jailbroken software failures.
* **Mandatory Documents Required**: Proof of purchase (bank statement or invoice), official repair shop itemized estimate/receipt, device IMEI/serial number photo, police report (for theft).
* **Validation & Fraud Rules**:
  * IMEI/Serial number on repair receipt must match policy record.
  * Carrier network IMEI blacklist confirmation required for theft claims.
* **Deductible & Co-Pay**: 20% co-pay of repair/replacement cost; minimum $50 deductible; maximum 2 claims per rolling 12 months.

---

#### 1.3 Auto & Motor Vehicle Mobility
* **Coverage Mechanism**: Supplemental auto insurance covering collision excess, roadside assistance, towing, windshield repair, and temporary rental car reimbursement.
* **✅ Included Items / Covered Objects**:
  * Collision excess / deductible reimbursement for primary auto insurance claims.
  * Windshield & auto glass chip repair or full replacement.
  * Emergency roadside towing, battery jump-starts, flat tire replacement, and fuel delivery.
  * Daily rental car allowance ($50/day) while personal vehicle is in repair shop following a covered accident.
* **❌ Excluded Items / Objects (Not Covered)**:
  * Routine mechanical breakdown, engine wear, or oil/maintenance service.
  * Accidents occurring while driving under the influence of alcohol or drugs.
  * Commercial rideshare or delivery driving (Uber, Lyft, DoorDash) unless commercial auto rider enabled.
  * Driving without a valid driver's license.
* **Mandatory Documents Required**: Primary insurer claim settlement letter, police accident report, repair shop invoice, rental car agreement, valid driver's license copy.
* **Validation & Fraud Rules**:
  * Primary insurer must approve claim before excess reimbursement is disbursed.
* **Deductible & Co-Pay**: $0 deductible for windshield repairs; $250 deductible for collision excess claims.

---

#### 1.4 Personal Health & Accident Insurance
* **Coverage Mechanism**: Direct reimbursement for outpatient specialist visits, prescription drugs, emergency dental, and daily hospital cash benefits.
* **✅ Included Items / Covered Objects**:
  * Specialist consultations (cardiologist, dermatologist, orthopedist) referred by GP.
  * Prescription pharmaceuticals and emergency vaccinations.
  * Emergency dental pain relief or accidental tooth breakage treatment.
  * Daily cash stipend ($150/day) for inpatient hospital stays exceeding 24 hours.
* **❌ Excluded Items / Objects (Not Covered)**:
  * Elective cosmetic surgery, non-prescribed vitamins, or dietary supplements.
  * Experimental medical treatments not approved by health authorities (FDA/EMA).
  * Routine eye exams or designer eyeglass frames (unless optical rider added).
* **Mandatory Documents Required**: GP referral letter, itemized medical invoice, pharmacy receipt, discharge summary (for hospital stays).
* **Validation & Fraud Rules**:
  * Referral letter must be dated prior to specialist consultation.
* **Deductible & Co-Pay**: $20 co-pay per clinic visit; 80% coverage rate for prescription drugs.

---

#### 1.5 Home & Mortgage Protection
* **Coverage Mechanism**: Protects residential building structures, home contents, and covers mortgage payments during unexpected involuntary unemployment or disability.
* **✅ Included Items / Covered Objects**:
  * Building structural damage from fire, storm, burst pipes, or fallen trees.
  * Home contents (furniture, TV/appliances, clothing) damaged or stolen.
  * Alternative temporary accommodation allowance if home becomes uninhabitable.
  * Involuntary redundancy / unemployment mortgage payment protection (up to 6 months).
* **❌ Excluded Items / Objects (Not Covered)**:
  * Gradual wear and tear, mold, rot, termite damage, or lack of maintenance.
  * Flood damage in designated high-risk flood zones unless flood rider purchased.
  * Voluntary resignation or termination for cause (for mortgage payment protection).
* **Mandatory Documents Required**: Property damage photos, repair contractor estimates, employment termination letter / severance notice, mortgage statement.
* **Validation & Fraud Rules**:
  * Unemployment claims require monthly proof of active job search / government registration.
* **Deductible & Co-Pay**: $500 deductible per property damage incident.

---

## 2. Commercial & SME (Small Business) Insurance Lines

### 2.1 Commercial Property & Inventory Spoilage
* **Coverage Mechanism**: Reimburses small businesses for damage to physical storefronts, office equipment, machinery, and perishable stock.
* **✅ Included Items / Covered Objects**:
  * Storefront glass, commercial office furniture, POS terminals, and servers.
  * Manufacturing machinery, kitchen equipment, and refrigeration units.
  * Perishable raw materials, food inventory, or pharmaceutical stock lost to power outages or cold storage failure (> 4 hours).
* **❌ Excluded Items / Objects (Not Covered)**:
  * Employee theft or internal embezzlement (covered under Crime/Fidelity insurance instead).
  * Normal inventory shrinkage or unexplained stock counts.
  * Equipment failure caused by failure to perform mandatory routine maintenance.
* **Mandatory Documents Required**: POS inventory ledger, cold storage temperature sensor log, power company outage verification letter, repair technician report.
* **Validation & Fraud Rules**:
  * Power company verification required to confirm utility blackout timeline.
* **Deductible & Co-Pay**: $500 deductible per incident; 90% coverage for perishable inventory.

---

### 2.2 Business Interruption & Revenue Loss
* **Coverage Mechanism**: Replaces lost net operating income and ongoing fixed costs (rent, payroll) when a business is forced to shut down due to a covered physical event.
* **✅ Included Items / Covered Objects**:
  * Lost net profit during forced closure period following fire, flood, or severe storm.
  * Continued fixed operating expenses (employee salaries, commercial lease rent, utility base fees).
  * Reasonable relocation costs to temporary operating facilities.
* **❌ Excluded Items / Objects (Not Covered)**:
  * Revenue loss caused by economic downturns, market competition, or changing consumer demand.
  * Closures mandated by government health lockdowns (unless epidemic rider purchased).
* **Mandatory Documents Required**: Prior 12 months historical profit & loss (P&L) statements, tax returns, lease agreement, proof of fixed payroll, disaster inspection certificate.
* **Validation & Fraud Rules**:
  * Audited financial P&L used in code sandbox to compute historical daily net revenue baseline.
* **Deductible & Co-Pay**: 48-hour waiting period (elimination period); 100% coverage of verified net profit loss up to policy cap ($250,000).

---

### 2.3 Cyber Risk, Ransomware & Data Breach
* **Coverage Mechanism**: Covers crisis response, legal fees, forensic investigations, ransomware extortion negotiation, and customer notification costs after a cyber incident.
* **✅ Included Items / Covered Objects**:
  * IT forensic investigator fees to identify breach source and clear malware.
  * Mandatory customer notification, credit monitoring service costs, and PR crisis management.
  * Ransomware extortion reimbursement (where legally permitted) and data restoration costs.
  * Third-party liability defense costs for leaked customer PII/financial data.
* **❌ Excluded Items / Objects (Not Covered)**:
  * Fines levied by regulatory bodies for non-compliance prior to breach (e.g. unpatched known vulnerabilities).
  * Future lost contract value or reputational damage beyond direct PR costs.
* **Mandatory Documents Required**: Incident response log, forensic IT report, regulatory notification log, ransom payment authorization record, legal counsel invoices.
* **Validation & Fraud Rules**:
  * Sanctions screening tool executed prior to approving any ransomware extortion payout.
* **Deductible & Co-Pay**: $1,000 deductible; sub-limit of $100,000 for ransomware payouts.

---

### 2.4 Employer Liability & Worker Protection
* **Coverage Mechanism**: Protects business owners against legal liability and medical claims arising from employee work-related injuries or occupational illnesses.
* **✅ Included Items / Covered Objects**:
  * Medical bills and rehabilitation expenses for employees injured on job premises or client sites.
  * Disability wage replacement during recovery.
  * Legal defense costs and court settlement judgments from workplace injury lawsuits.
* **❌ Excluded Items / Objects (Not Covered)**:
  * Intentional self-inflicted injuries or injuries resulting from workplace fights/horseplay.
  * Injuries occurring while commuting to/from work (unless in company-provided transport).
* **Mandatory Documents Required**: Incident injury report, OSHA/safety authority notification, medical attending physician statement, employee payroll records.
* **Validation & Fraud Rules**:
  * Incident report must be logged within 48 hours of injury occurrence.
* **Deductible & Co-Pay**: $250 per claim; 100% medical expense coverage.

---

## 3. Private Banking & High-Net-Worth (HNW) Insurance Lines

### 3.1 Fine Art, Jewelry & Luxury Collectibles
* **Coverage Mechanism**: Worldwide "all-risk" coverage for high-value personal assets, luxury goods, and fine art on an agreed-value basis.
* **✅ Included Items / Covered Objects**:
  * Fine art paintings, sculptures, antique furniture, and rare wine collections.
  * Luxury watches (Rolex, Patek Philippe), diamond jewelry, and haute joaillerie.
  * Accidental breakage, disappearance, theft, or transit damage worldwide.
* **❌ Excluded Items / Objects (Not Covered)**:
  * Natural inherent vice, gradual fading from sunlight, or temperature/humidity deterioration.
  * Damage caused by uncertified restoration or cleaning attempts.
* **Mandatory Documents Required**: Certified appraisal report (within 3 years), high-resolution photos, purchase invoice, vault storage certificate, police report (if stolen).
* **Validation & Fraud Rules**:
  * Payout based on pre-agreed appraisal value on file in bank memory vault.
* **Deductible & Co-Pay**: $0 or $1,000 optional deductible for lower premiums; agreed payout value set at policy inception.

---

### 3.2 Marine & Aviation Assets
* **Coverage Mechanism**: Hull, machinery, and third-party liability coverage for private yachts, luxury motorboats, and private aircraft.
* **✅ Included Items / Covered Objects**:
  * Yacht hull damage, engine machinery failure, grounding, and marine salvage costs.
  * Private jet / turboprop airframe damage, jet engine ingestion, and hangar damage.
  * Passenger bodily injury and third-party property damage liability.
* **❌ Excluded Items / Objects (Not Covered)**:
  * Operating vessel or aircraft outside designated geographical navigational limits without notification.
  * Chartering vessel for commercial hire without commercial marine endorsement.
* **Mandatory Documents Required**: Captain / pilot logbook, official marine/aviation surveyor loss report, vessel/aircraft maintenance history, Coast Guard / Aviation Authority report.
* **Validation & Fraud Rules**:
  * Telemetry / AIS GPS logs verified against authorized navigation zone boundaries.
* **Deductible & Co-Pay**: 1% of total agreed hull value per incident.

---

### 3.3 Key-Person Executive Life & Loan Collateral
* **Coverage Mechanism**: High-limit life and disability protection taken by companies or private banking clients on key executives to secure commercial loans or fund buy-sell agreements.
* **✅ Included Items / Covered Objects**:
  * Lump-sum debt payoff for bank loans secured against key executive's active involvement.
  * Executive recruitment & business stabilization funding following key-person death or permanent disability.
* **❌ Excluded Items / Objects (Not Covered)**:
  * Death within 2 years of policy inception due to suicide.
  * Fraudulent misrepresentation of executive health status during medical underwriting.
* **Mandatory Documents Required**: Official death certificate or permanent disability medical panel report, corporate loan agreement, board resolution, corporate registry extract.
* **Validation & Fraud Rules**:
  * Payout disbursed directly into bank commercial loan account as debt settlement.
* **Deductible & Co-Pay**: $0 deductible; 100% lump-sum payout of policy face value ($1M–$50M).
