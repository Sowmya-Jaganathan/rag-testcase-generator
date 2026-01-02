

#  File-Based Multimodal RAG for Test Case / Use Case Generation

##  Overview

This project implements a **file-based Retrieval-Augmented Generation (RAG) system** that generates **use cases / test cases** from requirement documents such as text files, PDFs, and images.

Instead of relying on the LLM’s internal knowledge, the system **retrieves relevant context from provided files first** and then generates structured, grounded test cases.
This approach significantly **reduces hallucination** and ensures outputs are evidence-based.

---

##  Problem Statement

Given multiple input sources (PRDs, error code docs, UI screenshots, etc.), QA engineers often manually analyze documents to write test cases.
This project automates that process by:

* Ingesting requirement files
* Retrieving only relevant content for a user query
* Generating structured test cases grounded in the retrieved context

---

##  What is RAG?

**Retrieval-Augmented Generation (RAG)** is a technique where:

1. Documents are searched first (retrieval)
2. Only relevant content is passed to the AI model
3. The AI generates responses strictly using that context

This prevents hallucination and improves accuracy.

---

##  Architecture (High Level)

```
User Query
   ↓
Retriever (FAISS + Embeddings)
   ↓
Relevant Document Chunks
   ↓
Generator (AI / Fallback)
   ↓
Structured Test Cases (JSON)
```

---

##  Project Structure

```
rag-testcase-generator/
├── data/
│   └── sample_docs/
│       ├── Signup_PRD.txt
│       └── Signup_Errors.txt
│
├── ingestion/
│   ├── text_loader.py
│   └── ingest.py
│
├── retrieval/
│   ├── chunker.py
│   ├── vector_store.py
│   └── retriever.py
│
├── generation/
│   ├── prompt.py
│   └── generator.py
│
├── guards/
│   └── context_guard.py
│
├── app.py
├── ui.py
├── requirements.txt
├── README.md
└── .env.example
```

---

##  Tech Stack

* **Language:** Python
* **RAG Framework:** LangChain
* **Vector Store:** FAISS (local)
* **Embeddings:** Sentence Transformers (local model)
* **LLM:** OpenAI (optional, fallback supported)
* **UI:** Streamlit
* **OCR (optional):** Tesseract
* **Environment Management:** python-dotenv

---

##  Supported Input Types

* Text / Markdown (`.txt`, `.md`)
* PDF documents
* Images (`.png`, `.jpg`) via OCR (extendable)
* File-based local ingestion (no external DB required)

---

##  Setup Instructions

### 1 Clone the Repository

```bash
git clone <your-repo-url>
cd rag-testcase-generator
```

### 2️ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate   # Windows
```

### 3️ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️ (Optional) Configure OpenAI

Create a `.env` file:

```txt
OPENAI_API_KEY=your_api_key_here
```

> The project works even **without OpenAI** using a fallback generator.

---

##  How to Run

### CLI Mode

```bash
python app.py
```

Enter query:

```
Create use cases for user signup
```

---

### UI Mode (Recommended)

```bash
streamlit run ui.py
```

Features:

* Query input
* JSON test case output
* Debug view showing retrieved chunks

---

##  Sample Query

```
Create use cases for user signup
```

---

##  Sample Output (JSON)

```json
{
  "Use Case Title": "User Signup with Email and Password",
  "Goal": "Allow a new user to create an account using email and password",
  "Preconditions": ["User is not logged in"],
  "Test Data": {
    "Valid Email": "newuser@example.com",
    "Valid Password": "StrongPass123"
  },
  "Steps": [
    "Open signup page",
    "Enter email",
    "Enter password",
    "Click signup"
  ],
  "Expected Results": [
    "Account created successfully",
    "Verification email sent"
  ],
  "Negative Cases": [
    "Duplicate email",
    "Weak password"
  ],
  "Boundary Cases": [
    "Password length = 8",
    "Max email length"
  ]
}
```

---

##  Safeguards & Guardrails

* **Retrieval-first design** (no direct LLM answering)
* **Context-only generation**
* **Minimum evidence threshold**
* **Fallback generator when LLM quota is unavailable**
* **Debug mode to inspect retrieved chunks**
* **No prompt injection from documents**

---

##  Observability & Debugging

* Console logs during ingestion and retrieval
* Debug view in UI to inspect retrieved context
* Modular design for easy testing and extension

---

##  Evaluation Readiness

The project demonstrates:

* Correct RAG flow
* Grounded test case generation
* Clean architecture
* Practical safeguards
* Developer-friendly setup

---

##  Future Enhancements

* Hybrid search (keyword + vector)
* File upload via UI
* Reranking and confidence scoring
* Automated evaluation metrics
* Full multimodal vision models

---

##  Recent Enhancements

- Added support for **Login use case and test case generation**
- Supports **multiple feature documents** (Signup & Login)
- Implemented **OCR-based ingestion** for UI screenshots (PNG/JPG)
- Query-aware generation of **multiple structured use cases**
- Streamlit UI shows **retrieved context** for transparency and debugging


##  Notes

* Local embeddings are used to avoid network and quota limitations.
* Generation layer is modular and can be swapped with any LLM.
* UI is intentionally minimal as per assignment guidance.

---

##  Author

**Sowmya Jaganathan**
AI & Data Science Student |
Machine Learning | RAG | QA 

---


