import json
import pandas as pd

scores = []

retrieval_keywords = [
    "retrieval", "ranking", "recommendation",
    "search", "embeddings", "vector",
    "pinecone", "milvus", "faiss",
    "weaviate", "qdrant"
]

with open("candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        c = json.loads(line)

        score = 0

        text = c["profile"].get("summary", "").lower()

        for job in c["career_history"]:
            text += " " + job.get("description", "").lower()

        retrieval_hits = sum(
            1 for k in retrieval_keywords if k in text
        )

        score += retrieval_hits * 10

        years = c["profile"].get(
            "years_of_experience", 0
        )

        if 5 <= years <= 9:
            score += 50

        signals = c["redrob_signals"]

        if signals.get("open_to_work_flag"):
            score += 20

        score += (
            signals.get(
                "recruiter_response_rate", 0
            ) * 50
        )

        score += signals.get(
            "github_activity_score", 0
        )

        scores.append(
            (
                c,
                round(score, 2)
            )
        )

scores.sort(
    key=lambda x: (-x[1], x[0]["candidate_id"])
)

top100 = scores[:100]

rows = []

for rank, (candidate, score) in enumerate(
    top100,
    start=1
):

    title = candidate["profile"][
        "current_title"
    ]

    years = candidate["profile"][
        "years_of_experience"
    ]

    reasoning = (
        f"{title} with {years} yrs; "
        f"retrieval/ranking experience; "
        f"active candidate"
    )

    rows.append({
        "candidate_id":
            candidate["candidate_id"],
        "rank":
            rank,
        "score": score / 300,
        "reasoning":
            reasoning
    })

df = pd.DataFrame(rows)

df.to_csv(
    "submission.csv",
    index=False
)

print(
    "submission.csv created"
)