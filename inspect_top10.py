import json

target_ids = {
    "CAND_0002025",
    "CAND_0017960",
    "CAND_0018499",
    "CAND_0018722",
    "CAND_0028793"
}

with open("candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        c = json.loads(line)

        if c["candidate_id"] in target_ids:
            print("\n" + "="*80)
            print(c["candidate_id"])
            print(c["profile"]["current_title"])
            print(c["profile"]["years_of_experience"])
            print(c["profile"]["summary"][:300])