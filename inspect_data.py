import json

with open("candidates.jsonl", "r", encoding="utf-8") as f:
    first_candidate = json.loads(next(f))

print("Candidate Fields:")
for key in first_candidate.keys():
    print("-", key)

print("\nSample Candidate:")
print(json.dumps(first_candidate, indent=2)[:3000])