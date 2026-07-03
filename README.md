# CiteMind
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Database-5A45FF?style=for-the-badge)
![Sentence Transformers](https://img.shields.io/badge/Sentence--Transformers-Embeddings-orange?style=for-the-badge)
![RAGAS](https://img.shields.io/badge/RAGAS-Evaluation-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

A production-ready Retrieval-Augmented Generation (RAG) system built from scratch to understand every component of modern AI engineering.

## Current Progress
![Status](https://img.shields.io/badge/Status-Active%20Development-success?style=for-the-badge)
![Progress](https://img.shields.io/badge/Progress-30%25-blueviolet?style=for-the-badge)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge)

-  Document Ingestion (Competed)
-  Text Cleaning
-  Chunking
-  Embeddings
-  Vector Database
-  Hybrid Retrieval
-  Re-ranking
-  Evaluation
-  CI/CD

## Tech Stack

- Python
- LangChain
- ChromaDB
- PyMuPDF
- Sentence Transformers
- RAGAS

## Features

- PDF
- Markdown
- HTML
- Plain Text

Each document is converted into LangChain `Document` objects while preserving rich metadata such as:

- filename
- source path
- page number (PDFs)
- file type

---

### Document Cleaning Pipeline

The preprocessing pipeline currently performs:

- Unicode normalization (NFKC)
- Hyphenated word repair
- Multiple whitespace normalization
- Blank line normalization
- Trailing whitespace removal
- Metadata preservation

Designed with a modular architecture for future document-specific cleaning.



## Project Goal

Build a production-quality RAG pipeline while learning every architectural component rather than relying on tutorials.

## Project Structure

```text
CiteMind/
│
├── data/
│   └── raw/
│       ├── pdf_files/
│       ├── markdown_files/
│       ├── html_files/
│       └── text_files/
│
├── src/
│   ├── chunking/
│   ├── cleaning/
│   ├── embeddings/
│   ├── evaluation/
│   ├── ingestion/
│   ├── llm/
│   ├── retrieval/
│   └── utils/
│
├── prompts/
├── evals/
├── tests/
└── README.md
```

# Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/Divyansh-Aryaa/citemind.git
cd citemind
```

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

macOS / Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Add Your Documents

Place your files inside:
> This folder structure should match or you could change the code according to your folder structure 

```text

data/raw/

├── pdf_files/
├── markdown_files/
├── html_files/
└── text_files/
```

Supported formats:

- PDF
- Markdown (.md)
- HTML (.html)
- Plain Text (.txt)

---

## 5. Run the Ingestion Pipeline

```bash
python -m src.ingestion.loader
```

You should see a summary showing the number of files processed and LangChain `Document` objects created.


## Current Pipeline

```text
Raw Documents
      │
      ▼
Document Ingestion
      │
      ▼
LangChain Documents
      │
      ▼
Cleaning & Preprocessing
      │
      ▼
Clean Documents
```

## Sample Data

This repository intentionally does not include the document corpus used during development.

Reasons:

- Keep the repository lightweight.
- Avoid distributing copyrighted material.
- Encourage users to experiment with their own datasets.

Simply place your own documents inside `data/raw/` following the supported folder structure.
