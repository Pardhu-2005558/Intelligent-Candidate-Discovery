import json

target_id = "CAND_0002025"

with open("candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        c = json.loads(line)

        if c["candidate_id"] == target_id:
            print(json.dumps(c, indent=2))
            break