# week6_lab.py
# Author: Theo

records = [
    {"name": "Ransom", "amount": 1200, "status": "Pending"},
    {"name": "Bryce", "amount": 450, "status": "Pending"},
    {"name": "Joe", "amount": 3500, "status": "Approved"},
    {"name": "Ben", "amount": 89, "status": "Pending"},
    {"name": "Wag", "amount": 2200, "status": "Pending"},
]

total = 0
flagged = []
high_value = []

for rec in records:
    if rec["status"] == "Pending":  # only count pending ones
        total += rec["amount"]
        if rec["amount"] > 1000:  # rule 1: needs review
            flagged.append(rec)
        if rec["amount"] > 2000:  # rule 2: high-value
            high_value.append(rec)

summary = (
    f"Pending total: ${total:,.2f}\n"
    f"Needs review: {len(flagged)}\n"
    f"High-value: {len(high_value)}\n"
)
print(summary)

with open("week6_summary.txt", "w") as f:
    f.write(summary)
