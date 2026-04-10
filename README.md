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
│
├── raw_data/
│ ├── raw/
│ │ ├── products.json
│ │ ├── users.json
│ │ └── carts.json
│ │
│ ├── process_data/
│ │ ├── products.csv
│ │ ├── users.csv
│ │ └── carts.csv
│
├── api_etl/
│ └── api_extraction.py
│
├── rag_app/
│ └── app.py
│
├── e-commerce_sales_dashboard/
│ └── E-Commerce Sales Dashboard.pdf
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

pip install -r requirements.txt
python -m streamlit run rag_app/app.py

---

## 📊 Dashboard

The Power BI dashboard provides key business insights from the processed e-commerce data.

**Key Metrics**:

- Total Revenue
- Top Selling Products
- Category-wise Distribution
- User Purchase Behavior

**Insights**:
- Identified high-value products and categories
- Analyzed customer purchasing patterns
- Enabled data-driven decision making

---

## 📡 Data Source

- The data used in this project is sourced from the FakeStore API.
- API Endpoint: https://fakestoreapi.com/
- Data Format: JSON
Data Entities:
Products
Users
Carts

The API provides mock e-commerce data used for building and testing the pipeline.

---

## 💡 Key Features
- End-to-end data pipeline using AWS services
- Data ingestion from API
- ETL processing using AWS Glue (PySpark)
- Data stored in Parquet format
- SQL analytics using Athena
- Power BI dashboard
- AI chatbot using RAG

---

## 🧠 Learnings

- Built scalable data pipeline
- Worked with JSON & structured data
- Used PySpark for ETL
- Performed SQL analysis
- Built dashboard
- Learned embeddings & vector databases
- Built RAG chatbot

---
