import streamlit as st
import pandas as pd
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Title
st.title("🛒 E-Commerce AI Chatbot")

# Load data
products = pd.read_csv("ecommerce-data-engineering-project/process_data/products.csv")

# Convert to text
docs = []
for i, row in products.iterrows():
    text = f"Product {row['title']} costs {row['price']} in category {row['category']}"
    docs.append(text)

# Create embeddings
embeddings = HuggingFaceEmbeddings()

# Create vector DB
vector_db = FAISS.from_texts(docs, embeddings)

# User input
query = st.text_input("Ask a question about products:")

# Response
if query:
    results = vector_db.similarity_search(query)
    
    st.subheader("Answer:")
    st.write(results[0].page_content)
