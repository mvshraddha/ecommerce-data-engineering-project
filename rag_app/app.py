import pandas as pd
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

# STEP 1: Load data
products = pd.read_csv("products.csv")

# STEP 2: Convert to text
docs = []

for i, row in products.iterrows():
    text = f"Product {row['title']} costs {row['price']} in category {row['category']}"
    docs.append(text)

# STEP 3: Use FREE embeddings (no API key)
embeddings = HuggingFaceEmbeddings()

# STEP 4: Create vector DB
vector_db = FAISS.from_texts(docs, embeddings)

# STEP 5: Ask question
query = input("Ask your question: ")

results = vector_db.similarity_search(query)

print("\nAnswer:")
print(results[0].page_content)
