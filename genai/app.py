from bedrocks import analyze_claim


claim = """
Customer vehicle damaged due to heavy rainfall while parked.

Estimated repair cost: ₹1,80,000

Policy: Comprehensive

No previous claims in the last 3 years.

Policyholder has been with the company for 5 years.
"""


print(analyze_claim(claim))
