import json
import pandas as pd

scores = []

retrieval_keywords = [
    "retrieval",
    "ranking",
    "recommendation",
    "search",
    "embeddings",
    "vector",
    "pinecone",
    "milvus",
    "faiss",
    "weaviate",
    "qdrant"
]

product_companies = [
    "product",
    "saas",
    "marketplace",
    "startup"
]

forbidden_titles = [
    "marketing",
    "sales",
    "hr",
    "recruiter"
]

with open("candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:

        c = json.loads(line)

        score = 0

        text = c["profile"].get("summary", "").lower()

        for job in c["career_history"]:
            text += " " + job.get("description", "").lower()

        # Retrieval score
        retrieval_hits = sum(
            1 for k in retrieval_keywords if k in text
        )
        score += retrieval_hits * 10

        # Experience score
        years = c["profile"].get(
            "years_of_experience", 0
        )

        if 5 <= years <= 9:
            score += 50
        else:
            score += max(0, 50 - abs(years - 7) * 5)

        # Open to work
        if c["redrob_signals"].get(
            "open_to_work_flag", False
        ):
            score += 20

        # Recruiter response rate
        score += (
            c["redrob_signals"].get(
                "recruiter_response_rate", 0
            ) * 50
        )

        # GitHub activity
        score += c["redrob_signals"].get(
            "github_activity_score", 0
        )

        # Penalty for wrong titles
        title = c["profile"].get(
            "current_title", ""
        ).lower()

        if any(t in title for t in forbidden_titles):
            score -= 100

        scores.append(
            (
                c["candidate_id"],
                round(score, 2)
            )
        )

scores.sort(
    key=lambda x: x[1],
    reverse=True
)

top100 = scores[:100]

df = pd.DataFrame(
    top100,
    columns=["candidate_id", "score"]
)

print(df.head(20))

df.to_csv(
    "top100_candidates.csv",
    index=False
)

print("\nSaved top100_candidates.csv")