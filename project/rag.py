from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Embedding model (correct one)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load data
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Better chunking
chunks = [c.strip() for c in text.split("\n") if c.strip()]

# Create embeddings
embeddings = model.encode(chunks)
embeddings = np.array(embeddings).astype("float32")

# FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

def retrieve(query, k=3):
    q_emb = model.encode([query])
    q_emb = np.array(q_emb).astype("float32")

    distances, indices = index.search(q_emb, k)

    return [chunks[i] for i in indices[0]]