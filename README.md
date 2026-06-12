# ⚖️ AI Legal Assistant (CrewAI + FastAPI + ChromaDB)

An AI-powered Legal Assistant built using CrewAI that analyzes legal issues, retrieves relevant IPC sections using RAG, finds legal precedents, and generates formal legal documents such as police complaints.

---

## 🚀 Features

* Case understanding and legal issue extraction
* IPC section retrieval using Chroma Vector Database
* Legal precedent search using Tavily
* Legal complaint/document drafting
* FastAPI backend for integration with React or other frontends
* Streamlit UI for local testing
* CrewAI multi-agent workflow

---

# 🏗️ Architecture

User Input
↓
FastAPI / Streamlit
↓
CrewAI
↓
Case Intake Agent
↓
IPC Section Agent
↓
IPC Search Tool (ChromaDB)
↓
Legal Precedent Agent
↓
Legal Precedent Search Tool (Tavily)
↓
Legal Drafting Agent
↓
Final Legal Document

---

# 🤖 Agents

## 1. Case Intake Agent

Responsibilities:

* Understand the legal issue
* Extract key facts
* Identify legal domain
* Generate structured case summary

Output:

```json
{
  "case_type": "...",
  "legal_domain": "...",
  "summary": "..."
}
```

## 2. IPC Section Agent

Responsibilities:

* Analyze case summary
* Retrieve relevant IPC sections
* Use ChromaDB vector search

Tool Used:

* IPC Sections Search Tool

## 3. Legal Precedent Agent

Responsibilities:

* Search relevant case laws
* Gather precedent information

Tool Used:

* Legal Precedent Search Tool

## 4. Legal Document Drafting Agent

Responsibilities:

* Generate legal complaint
* Reference IPC sections
* Incorporate precedent information

Output:

* Formal legal document

---

# 🛠 Tools

## IPC Sections Search Tool

Uses:

* ChromaDB
* HuggingFace Embeddings

Purpose:

Retrieve IPC sections relevant to a legal query using semantic similarity search.

Example:

Input:

```text
Motorcycle theft outside house
```

Output:

```json
[
  {
    "section": 379,
    "section_title": "Punishment for theft"
  }
]
```

---

## Legal Precedent Search Tool

Uses:

* Tavily Search API

Purpose:

Search Indian legal precedent cases from trusted legal sources.

Sources:

* indiankanoon.org

---

# 🧠 RAG Pipeline

IPC data is stored inside:

```text
knowledge/ipc.json
```

The vector database is generated using:

```bash
python ipc_vectordb_builder.py
```

This creates:

```text
vectordb/
├── chroma.sqlite3
└── collection files
```

The IPC Section Agent queries this database during execution.

---

# ⚙️ Tech Stack

### Backend

* FastAPI
* CrewAI
* ChromaDB
* LangChain

### LLM

* Groq
* Llama 3.1 70B Versatile

### Search

* Tavily

### Embeddings

* sentence-transformers/all-MiniLM-L6-v2

### Frontend

* Streamlit
* React (future integration)

---

# 📁 Project Structure

```text
legalassistant/
│
├── knowledge/
│   ├── ipc.json
│   └── user_preference.txt
│
├── vectordb/
│
├── src/legalassistant/
│   ├── config/
│   │   ├── agents.yaml
│   │   └── tasks.yaml
│   │
│   ├── tools/
│   │   ├── ipc_sections_search_tool.py
│   │   └── legal_precedent_search_tool.py
│   │
│   ├── api.py
│   ├── crew.py
│   └── main.py
│
├── app.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key

MODEL=groq/llama-3.1-70b-versatile

IPC_JSON_PATH=knowledge/ipc.json
PERSIST_DIRECTORY_PATH=vectordb
IPC_COLLECTION_NAME=ipc_collection
```

---

# ▶️ Local Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Build vector database:

```bash
python ipc_vectordb_builder.py
```

Run FastAPI:

```bash
uvicorn legalassistant.api:app --reload
```

Open:

```text
http://localhost:8000/docs
```

---

# 📡 API Endpoint

## Analyze Legal Case

POST

```text
/api/analyze
```

Request:

```json
{
  "user_input": "My motorcycle was stolen outside my house."
}
```

Response:

```json
{
  "case_summary": {},
  "ipc_sections": [],
  "precedents": "",
  "legal_document": ""
}
```

---

# 🌐 Deployment

Backend can be deployed on:

* Render
* Railway
* Fly.io
* AWS EC2

Recommended:

* Render (Free Tier)

Start Command:

```bash
uvicorn legalassistant.api:app --host 0.0.0.0 --port $PORT
```

---

# 🔮 Future Improvements

* React Frontend
* User Authentication
* PDF Generation
* Legal Chat History
* Multi-Language Support
* Citation Linking
* Case Management Dashboard

---

# 📜 Disclaimer

This project is intended for educational and informational purposes only.

It does not constitute legal advice and should not replace consultation with a licensed legal professional.
