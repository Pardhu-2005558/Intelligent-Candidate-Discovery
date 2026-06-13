import json

count = 0

retrieval_candidates = 0

keywords = [
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

with open("candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        text = ""

        text += candidate["profile"].get("summary", "") + " "

        for job in candidate["career_history"]:
            text += job.get("description", "") + " "

        text = text.lower()

        if any(k in text for k in keywords):
            retrieval_candidates += 1

        count += 1

print("Total candidates:", count)
print("Retrieval-related candidates:", retrieval_candidates)