# 🛒 E-Commerce Data Engineering Project with RAG Chatbot

## 📌 Overview
This project demonstrates an end-to-end data engineering pipeline built on AWS along with an AI-powered chatbot using Retrieval-Augmented Generation (RAG).

The system extracts e-commerce data from an API, processes it using AWS services, performs analytics, and enables natural language querying through a chatbot.

---

## 🚀 Architecture

API → S3 (Raw JSON) → AWS Glue (ETL - PySpark) → S3 (Parquet) → Athena (SQL) → Power BI (Dashboard) → RAG Chatbot (Streamlit + FAISS)

---

## ⚙️ Tech Stack

- **Cloud:** AWS S3, AWS Glue, AWS Athena  
- **Processing:** PySpark  
- **Languages:** Python, SQL  
- **Visualization:** Power BI  
- **AI/ML:** LangChain, FAISS, HuggingFace Embeddings  
- **App:** Streamlit  

---

## 📂 Project Structure
ecommerce-project/
│
├── data/
│ ├── raw/
│ │ ├── products.json
│ │ ├── users.json
│ │ └── carts.json
│ │
│ ├── processed/
│ │ ├── products.csv
│ │ ├── users.csv
│ │ └── carts.csv
│
├── etl/
│ └── api_extraction.py
│
├── rag/
│ └── app.py
│
├── dashboard/
│ └── dashboard.png
│
├── README.md
├── requirements.txt

---

## 🔄 Data Pipeline

1. Extracted data from FakeStore API (JSON format)
2. Stored raw data in AWS S3
3. Used AWS Glue (PySpark) for ETL processing
4. Converted data into Parquet format
5. Queried data using AWS Athena
6. Built dashboard in Power BI
7. Created RAG-based chatbot for querying data

---

## 🤖 RAG Chatbot

The chatbot allows users to ask questions in natural language and retrieves relevant information using vector similarity search.

### Example Queries:
- "Which product has highest price?"
- "Top products in electronics"
- "Show expensive items"

---

## ▶️ Run Chatbot Locally

```bash
pip install -r requirements.txt
python -m streamlit run rag/app.py
