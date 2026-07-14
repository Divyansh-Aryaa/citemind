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
![Progress](https://img.shields.io/badge/Progress-40%25-blueviolet?style=for-the-badge)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge)

-  Document Ingestion (Completed)
-  Text Cleaning (Completed)
-  Chunking (Completed)
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

### Intelligent Document Chunking

- RecursiveCharacterTextSplitter
- Configurable chunk size and overlap
- Metadata preservation across chunks
- Context-aware overlapping chunks
- Chunk statistics and validation



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
      │
      ▼
Document Chunking
      │
      ▼
Embeddings (To be completed)

```

## Sample Data

This repository intentionally does not include the document corpus used during development.

Reasons:

- Keep the repository lightweight.
- Avoid distributing copyrighted material.
- Encourage users to experiment with their own datasets.

Simply place your own documents inside `data/raw/` following the supported folder structure.

## Roadmap

- [x] Multi-format document ingestion
- [x] Modular document cleaning pipeline
- [x] Intelligent chunking with overlap
- [ ] Embedding generation
- [ ] ChromaDB integration
- [ ] Semantic retrieval
- [ ] Hybrid retrieval (BM25 + Vector)
- [ ] Cross-encoder reranking
- [ ] Citation generation
- [ ] RAG evaluation with RAGAS
- [ ] FastAPI / Streamlit interface
- [ ] CI/CD quality gates

# ============================================================
# CITEMIND — PROJECT SNAPSHOT
# Current Stage: Chunking V1 Complete
# Next Stage: Embeddings
# ============================================================


# ============================================================
# 1. PROJECT OVERVIEW
# ============================================================

Project Name:
CiteMind

Project Type:
Production-oriented Citation-Aware Retrieval-Augmented Generation (RAG) System

Primary Goal:
Build a complete RAG system from scratch while understanding and implementing
each architectural component individually rather than relying on a pre-built
end-to-end abstraction.

Core planned capabilities:

- Multi-format document ingestion
- Document cleaning and normalization
- Context-aware chunking
- Dense embeddings
- Vector database search
- BM25 keyword retrieval
- Hybrid retrieval
- Cross-encoder re-ranking
- LLM-based answer generation
- Exact source and page-level citations
- RAG evaluation using RAGAS
- Testing and CI/CD


# ============================================================
# 2. CURRENT PIPELINE ARCHITECTURE
# ============================================================

Current implemented pipeline:

Raw Documents
      |
      v
Document Ingestion
      |
      v
Document Cleaning
      |
      v
Document Chunking
      |
      v
[ NEXT: Embeddings ]
      |
      v
Vector Database
      |
      v
Dense Vector Search + BM25
      |
      v
Hybrid Retrieval
      |
      v
Cross-Encoder Re-ranking
      |
      v
LLM Answer Generation
      |
      v
Citation-Backed Response
      |
      v
RAGAS Evaluation


# ============================================================
# 3. CURRENT PROJECT STRUCTURE
# ============================================================

CiteMind/
|
|-- .gitignore
|-- README.md
|-- app.py
|-- config.py
|-- requirements.txt
|
|-- data/
|   |-- raw/
|       |-- pdf_files/
|       |-- markdown_files/
|       |-- html_files/
|       |-- text_files/
|
|-- src/
|   |
|   |-- ingestion/
|   |   |-- loader.py
|   |   |-- pdf_loader.py
|   |   |-- markdown_loader.py
|   |   |-- html_loader.py
|   |   |-- text_loader.py
|   |
|   |-- cleaning/
|   |   |-- cleaner.py
|   |   |-- utils.py
|   |   |-- header_footer.py
|   |   |-- html_cleaner.py
|   |   |-- pdf_cleaner.py
|   |
|   |-- chunking/
|       |-- splitter.py
|
|-- evals/
|-- prompts/
|-- tests/


# ============================================================
# 4. MODULE 1 — DOCUMENT INGESTION
# STATUS: COMPLETE
# ============================================================

Goal:
Load multiple document formats and convert them into a common representation:

    langchain_core.documents.Document

Supported formats:

- PDF (.pdf)
- Markdown (.md)
- Plain text (.txt)
- HTML (.html)


# ------------------------------------------------------------
# 4.1 LOADER ARCHITECTURE
# ------------------------------------------------------------

A central loader.py dynamically selects the correct loader according to the
file extension.

Concept:

SUPPORTED_LOADERS = {
    ".pdf": load_pdf,
    ".md": load_markdown,
    ".txt": load_text,
    ".html": load_html,
}

Flow:

Directory
    |
    v
Recursive file discovery using Path.rglob("*")
    |
    v
Read file extension
    |
    v
Find appropriate loader
    |
    v
Load into LangChain Document objects
    |
    v
Combine all Documents into one list


# ------------------------------------------------------------
# 4.2 LOAD_DOCUMENTS RETURN VALUE
# ------------------------------------------------------------

Originally, load_documents() returned only:

    all_documents

Later, ingestion statistics were added.

The function now returns:

    return all_documents, stats

Usage:

    docs, stats = load_documents(DATA_DIR)

This caused an important bug during cleaning development.

Incorrect:

    docs = load_documents(DATA_DIR)

Because docs became:

    (
        [Document, Document, ...],
        stats_dictionary
    )

Then cleaner.py attempted:

    doc.page_content

on a list/tuple-like structure, causing:

    AttributeError:
    'list' object has no attribute 'page_content'

Fix:

    docs, stats = load_documents(DATA_DIR)


# ------------------------------------------------------------
# 4.3 INGESTION STATISTICS
# ------------------------------------------------------------

The loader tracks actual files loaded by type:

stats = {
    "pdf": 0,
    "markdown": 0,
    "text": 0,
    "html": 0,
}

Important design decision:

For PDFs, one PDF can produce many Document objects because each page is
represented as an individual Document.

Therefore:

    stats["pdf"] += 1

counts PDF FILES.

Using:

    stats["pdf"] += len(docs)

would incorrectly count PDF pages as PDF files.


# ------------------------------------------------------------
# 4.4 HIDDEN AND UNSUPPORTED FILES
# ------------------------------------------------------------

Hidden files are ignored:

    if file.name.startswith("."):
        continue

Unsupported extensions are skipped with a warning.

This prevents files such as:

    .DS_Store

from entering the ingestion pipeline.


# ------------------------------------------------------------
# 4.5 METADATA PRESERVATION
# ------------------------------------------------------------

Each Document contains:

    page_content

and:

    metadata

Important metadata currently includes fields such as:

    source
    filename
    page
    file_type

PDF loaders may also produce:

    title
    author
    creator
    producer
    total_pages
    format
    keywords

Example:

metadata = {
    "source": "/path/to/Attention_Is_all_you_need.pdf",
    "filename": "Attention_Is_all_you_need.pdf",
    "page": 0,
    "file_type": "pdf"
}

This metadata is critical for future citation generation.


# ============================================================
# 5. CITATION DESIGN DECISION
# ============================================================

One major design goal is exact source and page-level citation.

Example future response:

    "Transformers use self-attention to process token relationships."

    Source:
    Attention_Is_all_you_need.pdf
    Page: 4

The PDF loader stores:

    metadata["page"] = 0

for the first page.

This is zero-indexed internally.

When showing citations to users later, it can be displayed as:

    metadata["page"] + 1

so internal page 0 becomes displayed page 1.


# ------------------------------------------------------------
# 5.1 CHUNK PAGE NUMBER DESIGN
# ------------------------------------------------------------

We discussed whether chunks from page 5 should use:

    5.1
    5.2
    5.3

This was rejected.

Reason:

There is no actual "page 5.2" in the source PDF, so this would create
confusing and inaccurate citations.

Final decision:

If page 5 creates six chunks:

    Chunk 1 -> page = 5
    Chunk 2 -> page = 5
    Chunk 3 -> page = 5
    Chunk 4 -> page = 5
    Chunk 5 -> page = 5
    Chunk 6 -> page = 5

All chunks preserve the real source page number.

We also discussed adding:

    chunk_index

but decided not to add it in V1 because there is no immediate downstream
requirement for it.

Principle followed:

    Do not add metadata without a concrete use case.


# ============================================================
# 6. MODULE 2 — DOCUMENT CLEANING
# STATUS: COMPLETE FOR V1
# ============================================================

Goal:

Normalize extracted text before chunking, embedding, and retrieval.

Pipeline:

Ingested Documents
        |
        v
Unicode Normalization
        |
        v
Hyphenation Repair
        |
        v
Leading/Trailing Whitespace Removal
        |
        v
Multiple Space Collapse
        |
        v
Excessive Blank Line Collapse
        |
        v
Trailing Line Whitespace Removal
        |
        v
Cleaned Documents


# ------------------------------------------------------------
# 6.1 CLEAN_DOCUMENTS
# ------------------------------------------------------------

Core interface:

    def clean_documents(
        documents: list[Document]
    ) -> list[Document]:

For every Document:

    text = doc.page_content

Cleaning rules are applied to text.

A new Document is then created:

    cleaned_doc = Document(
        page_content=text,
        metadata=doc.metadata.copy()
    )

Important:

Metadata is explicitly copied.

Therefore cleaning modifies text but preserves:

    source
    filename
    page
    file_type

This keeps future citations possible.


# ------------------------------------------------------------
# 6.2 UNICODE NORMALIZATION
# ------------------------------------------------------------

Implemented using:

    unicodedata.normalize("NFKC", text)

Purpose:

Normalize visually equivalent Unicode characters into a more consistent form.

Bug encountered:

Originally wrote:

    unicodedata.normalize("NFCK", text)

This caused:

    ValueError: invalid normalization form

Correct normalization form:

    NFKC


# ------------------------------------------------------------
# 6.3 HYPHENATION REPAIR
# ------------------------------------------------------------

Implemented using:

    re.sub(r"(\w)-\n(\w)", r"\1\2", text)

Example:

Before:

    transfor-
    mation

After:

    transformation

This is useful for text extracted from PDFs where words are broken across
line endings.

We verified this rule using actual extracted PDF content.

Before adding the rule, fewer characters were removed.

After adding it, one sample page showed:

    Characters Removed: 19

confirming that actual cleanup occurred.


# ------------------------------------------------------------
# 6.4 WHITESPACE CLEANING
# ------------------------------------------------------------

Rules implemented:

1. Remove leading/trailing document whitespace:

    text.strip()

2. Collapse multiple spaces and tabs:

    re.sub(r"[ \t]+", " ", text)

3. Collapse three or more newlines into two:

    re.sub(r"\n{3,}", "\n\n", text)

4. Remove trailing whitespace from individual lines.


# ------------------------------------------------------------
# 6.5 CLEANING UTILITIES REFACTOR
# ------------------------------------------------------------

Cleaning logic was moved into:

    src/cleaning/utils.py

Functions include:

    normalize_unicode()
    repair_hyphenation()
    collapse_spaces()
    collapse_blank_lines()
    remove_trailing_spaces()

Then cleaner.py imports them:

    from src.cleaning.utils import (
        normalize_unicode,
        repair_hyphenation,
        collapse_spaces,
        collapse_blank_lines,
        remove_trailing_spaces,
    )

This keeps cleaner.py focused on pipeline orchestration rather than individual
text transformations.


# ------------------------------------------------------------
# 6.6 HEADER/FOOTER GROUPING
# ------------------------------------------------------------

Created:

    src/cleaning/header_footer.py

Function:

    group_by_source(documents)

Uses:

    defaultdict(list)

Documents are grouped by:

    doc.metadata["source"]

Purpose:

Pages from the same source PDF can be analyzed together for repeated
headers and footers.

Example:

    PDF A -> 32 pages
    PDF B -> 13 pages
    PDF C -> 15 pages

Important observation:

The grouping function currently groups ALL supported file types by source,
not only PDFs.

Current output showed:

    Total Groups: 16

because there were 16 source files across PDF, Markdown, TXT, and HTML.


# ------------------------------------------------------------
# 6.7 CLEANING RESULTS
# ------------------------------------------------------------

At one point the cleaning pipeline produced:

    Documents Processed : 89
    Original Characters : 413,338
    Cleaned Characters  : 408,108
    Characters Removed  : 5,230
    Reduction Percentage: 1.27%

This confirmed that cleaning was modifying the corpus while preserving most
of its original content.


# ============================================================
# 7. MODULE 3 — CHUNKING
# STATUS: V1 COMPLETE
# ============================================================

Goal:

Split cleaned LangChain Document objects into smaller overlapping chunks
suitable for future embeddings and retrieval.

Pipeline:

Cleaned Documents
        |
        v
RecursiveCharacterTextSplitter
        |
        v
Overlapping Chunks
        |
        v
Metadata-Preserved LangChain Documents


# ------------------------------------------------------------
# 7.1 WHY CHUNKING IS NEEDED
# ------------------------------------------------------------

Sending entire documents to an LLM for every question would be:

- inefficient
- expensive
- slow
- imprecise for retrieval
- limited by model context windows

Instead, documents are split into smaller retrievable units.


# ------------------------------------------------------------
# 7.2 CURRENT SPLITTER
# ------------------------------------------------------------

Current implementation uses:

    RecursiveCharacterTextSplitter

Configuration:

    CHUNK_SIZE = 700
    CHUNK_OVERLAP = 100

    RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
    )

Current units:

    Characters, not tokens.

The current V1 uses character-based chunking.

Token-aware chunking may be explored later if justified by embedding model
and evaluation results.


# ------------------------------------------------------------
# 7.3 SPLITTER FACTORY
# ------------------------------------------------------------

Implemented:

    def create_text_splitter():

        return RecursiveCharacterTextSplitter(
            chunk_size=700,
            chunk_overlap=100,
            length_function=len,
        )

Then:

    def split_documents(
        documents: list[Document]
    ) -> list[Document]:

        splitter = create_text_splitter()
        return splitter.split_documents(documents)

This keeps splitter configuration separate from actual document splitting.


# ------------------------------------------------------------
# 7.4 WHY OVERLAP EXISTS
# ------------------------------------------------------------

Without overlap, a sentence could be divided like:

Chunk 1:

    Artificial intelligence improves healthcare because

Chunk 2:

    it helps doctors detect diseases earlier.

Each chunk has incomplete context.

With overlap, some text from the end of Chunk 1 is repeated at the beginning
of Chunk 2.

Trade-off:

    Slightly more duplicate text and vector storage

in exchange for:

    Better semantic continuity
    Better embedding context
    Better retrieval accuracy


# ------------------------------------------------------------
# 7.5 OVERLAP VERIFICATION
# ------------------------------------------------------------

Overlap was explicitly tested.

End of Chunk 1 contained:

    "...and topologies for multi-agent systems (MAS) is inherently complex.
    To automate the entire design"

Beginning of Chunk 2 contained:

    "and topologies for multi-agent systems (MAS) is inherently complex.
    To automate the entire design process..."

This verified that overlap is working correctly.


# ------------------------------------------------------------
# 7.6 METADATA PRESERVATION DURING CHUNKING
# ------------------------------------------------------------

RecursiveCharacterTextSplitter preserved parent metadata automatically.

Example first chunk metadata contained:

    source
    file_path
    total_pages
    title
    author
    page
    filename
    file_type

Therefore a retrieved chunk can still be traced back to:

    Exact source file
    Exact PDF page

This is fundamental to CiteMind's citation feature.


# ------------------------------------------------------------
# 7.7 CURRENT CHUNKING RESULTS
# ------------------------------------------------------------

After correcting malformed text files:

    Original Documents   : 89
    Total Chunks         : 726
    Average Chunk Length : 590.94
    Largest Chunk        : 700
    Smallest Chunk       : 13
    Average Chunks/Doc   : 8.16


# ------------------------------------------------------------
# 7.8 MEANING OF CHUNK METRICS
# ------------------------------------------------------------

Average Chunk Length:

    Total characters across chunks
    ------------------------------
         Number of chunks

Current:

    590.94 characters

Meaning:

A typical chunk contains approximately 591 characters.


Average Chunks per Document:

    Total chunks
    ------------
    Total original Documents

Current:

    726 / 89 = 8.16

Meaning:

Each original LangChain Document produces approximately 8.16 chunks on
average.

Important:

For PDFs, each page is currently represented as an original Document.

Therefore this is not necessarily:

    8.16 chunks per complete source file

It means:

    8.16 chunks per input LangChain Document on average.


# ============================================================
# 8. DATA QUALITY ISSUE DISCOVERED
# ============================================================

During chunk validation, the smallest chunk was initially:

    Length : 1
    Content: '\\'

Other chunks contained:

    \f0\fs24 \cf0

Investigation showed that some files had originally been RTF files whose
extensions were manually renamed to:

    .txt

Important lesson:

Renaming:

    document.rtf

to:

    document.txt

does NOT convert the file into plain text.

The internal file format remains RTF.

Analogy:

Renaming:

    movie.mp4

to:

    movie.pdf

does not convert the video into a PDF.


# ------------------------------------------------------------
# 8.1 FIX
# ------------------------------------------------------------

The malformed text files were replaced with genuine plain-text files.

After correction:

Before:

    Total Chunks   : 727
    Smallest Chunk : 1
    Content        : '\\'

After:

    Total Chunks   : 726
    Smallest Chunk : 13
    Content        : 'OCEAN SCIENCE'


# ------------------------------------------------------------
# 8.2 CURRENT 10 SMALLEST CHUNKS
# ------------------------------------------------------------

Examples:

    13 chars -> OCEAN SCIENCE
    16 chars -> MODERN ECONOMICS
    17 chars -> SPACE EXPLORATION
    20 chars -> HISTORY OF COMPUTING

These are legitimate section headings, not malformed chunks.

Decision:

Do not remove them automatically.

A small chunk is not necessarily a bad chunk.

Filtering should be based on semantic usefulness, not just length.


# ============================================================
# 9. CURRENT IMPLEMENTATION STATUS
# ============================================================

COMPLETED:

[✓] Multi-format document ingestion
[✓] PDF support
[✓] Markdown support
[✓] Plain text support
[✓] HTML support
[✓] Dynamic loader selection
[✓] File-type statistics
[✓] Hidden file skipping
[✓] Unsupported file handling
[✓] Metadata preservation
[✓] Page metadata preservation
[✓] Unicode normalization
[✓] Hyphenation repair
[✓] Whitespace normalization
[✓] Blank-line cleanup
[✓] Modular cleaning utilities
[✓] Source grouping foundation
[✓] Recursive character chunking
[✓] Configurable chunk size and overlap foundation
[✓] Chunk metadata propagation
[✓] Chunk overlap verification
[✓] Chunk statistics
[✓] Smallest-chunk validation
[✓] Input data quality debugging


# ============================================================
# 10. WHAT WE DELIBERATELY DID NOT ADD YET
# ============================================================

We intentionally avoided premature complexity.

NOT ADDED:

- Custom chunk IDs
- chunk_index metadata
- UUIDs
- Chunk hashes
- Timestamps
- Parent-child chunk mapping
- Multiprocessing
- Async chunking
- Different splitter for every format
- Token-based chunking
- Aggressive small-chunk filtering

Reason:

Do not add complexity without a concrete downstream requirement.

Current principle:

    Build -> Test -> Validate -> Move Forward -> Optimize with Evidence


# ============================================================
# 11. NEXT STAGE — EMBEDDINGS
# ============================================================

The next pipeline stage is:

    Chunks
       |
       v
    Embedding Model
       |
       v
    Numerical Vectors

Conceptually:

Text:

    "Transformers use self-attention."

becomes something like:

    [0.124, -0.582, 0.931, ..., 0.217]

This vector represents the semantic meaning of the text in a
high-dimensional numerical space.

Similar meanings should produce nearby vectors.

Example:

    "AI is transforming healthcare."

and:

    "Artificial intelligence is changing medicine."

should have semantically similar embeddings despite using different words.


# ============================================================
# 12. EMBEDDINGS — DECISIONS TO MAKE NEXT
# ============================================================

Before implementing embeddings, we should understand and decide:

1. Which embedding model should CiteMind use?

2. Should embeddings run locally or through an API?

3. What is embedding dimensionality?

4. How are 726 chunks embedded efficiently?

5. Should embedding be done one chunk at a time or in batches?

6. How do we verify that semantically similar text produces similar vectors?

7. How do we separate embedding generation from vector database storage?

Recommended architecture:

    src/
    |
    |-- embeddings/
        |-- embedder.py

Responsibility:

    List[Document]
          |
          v
    Extract chunk text
          |
          v
    Embedding model
          |
          v
    Dense numerical vectors


# ============================================================
# 13. AFTER EMBEDDINGS — VECTOR DATABASE
# ============================================================

Planned flow:

    726 chunks
         |
         v
    Generate embeddings
         |
         v
    Store:
        chunk text
        embedding vector
        metadata
         |
         v
    ChromaDB

Each stored item should conceptually contain:

    {
        "text": "Multi-agent systems...",
        "embedding": [...],
        "metadata": {
            "source": "...",
            "filename": "...",
            "page": 0,
            "file_type": "pdf"
        }
    }

The metadata is what eventually enables citations.


# ============================================================
# 14. AFTER VECTOR DATABASE — DENSE VECTOR SEARCH
# ============================================================

User asks:

    "How does self-attention work?"

Flow:

    User Query
        |
        v
    Query Embedding
        |
        v
    Compare against stored chunk embeddings
        |
        v
    Retrieve semantically similar chunks

Dense vector search is good at semantic similarity.

Example:

Query:

    "How is artificial intelligence used in medicine?"

Relevant chunk:

    "Machine learning models help doctors detect diseases."

Even though exact words differ, semantic similarity can retrieve the chunk.


# ============================================================
# 15. BM25 KEYWORD SEARCH
# ============================================================

Dense vector search is not perfect.

It may struggle with exact:

- product codes
- acronyms
- technical identifiers
- rare names
- exact terminology

BM25 is a sparse keyword retrieval algorithm.

It is useful when exact lexical matches matter.

Example query:

    "MAS optimization framework"

BM25 can strongly reward chunks containing those exact terms.


# ============================================================
# 16. HYBRID RETRIEVAL
# ============================================================

CiteMind's planned retrieval architecture:

                    User Query
                         |
             +-----------+-----------+
             |                       |
             v                       v
      Dense Vector Search       BM25 Search
             |                       |
             +-----------+-----------+
                         |
                         v
                  Result Fusion
                         |
                         v
              Cross-Encoder Re-ranking
                         |
                         v
                 Best Context Chunks

Why hybrid retrieval?

Dense search:

    Good at meaning.

BM25:

    Good at exact keywords.

Together:

    Better recall across semantic and lexical queries.


# ============================================================
# 17. CROSS-ENCODER RE-RANKING
# ============================================================

Initial retrieval may return many candidates.

Example:

    Vector Search -> Top 10
    BM25          -> Top 10

After fusion, a cross-encoder can score query-document pairs more precisely.

Flow:

    Query + Candidate Chunk
              |
              v
         Cross Encoder
              |
              v
        Relevance Score

Then candidates are reordered.

Goal:

Send only the highest-quality context to the LLM.


# ============================================================
# 18. ANSWER GENERATION AND CITATIONS
# ============================================================

Final retrieval results will still contain metadata.

Example:

    Chunk:
        "Self-attention allows..."

    Metadata:
        filename = "Attention_Is_all_you_need.pdf"
        page = 3

The LLM receives retrieved context.

Final response can include:

    Transformers use self-attention to model relationships between tokens.

    Source:
    Attention_Is_all_you_need.pdf, Page 4

Remember:

Internal page:

    3

Displayed PDF page:

    4

assuming zero-based page indexing from the loader.


# ============================================================
# 19. RAG EVALUATION
# ============================================================

Planned evaluation with RAGAS.

Metrics may include:

- Faithfulness
- Answer relevance
- Context precision
- Context recall

Goal:

Do not evaluate the RAG system based only on:

    "The answer looks good."

Instead, measure retrieval and generation quality systematically.


# ============================================================
# 20. TARGET FINAL CITEMIND RESUME VERSION
# STORE FOR AFTER PROJECT COMPLETION
# ============================================================

CiteMind — Citation-Aware RAG System [GitHub]

Tech Stack:
Python, LangChain, ChromaDB, Sentence Transformers, BM25, RAGAS

• Engineered a production-oriented RAG pipeline with multi-format document
  ingestion, preprocessing, context-aware chunking, and metadata preservation
  for exact source and page-level citations.

• Implemented hybrid retrieval combining dense vector search and BM25 keyword
  search, with cross-encoder re-ranking to improve retrieval relevance and
  answer grounding.

• Built citation-backed response generation with source traceability and
  RAGAS-based evaluation to measure retrieval quality, faithfulness, and
  answer relevance.

IMPORTANT:

This is the TARGET resume version.

Only use the full version after all claimed features are actually implemented
and tested.


# ============================================================
# 21. CURRENT RESUME-SAFE CITEMIND VERSION
# ============================================================

CiteMind — Citation-Aware RAG System [GitHub]

Tech Stack:
Python, LangChain, PyMuPDF, BeautifulSoup, NLP

• Developed a modular RAG document pipeline supporting PDF, HTML, Markdown,
  and TXT ingestion with metadata preservation for source and page-level
  citations.

• Built a reusable text preprocessing pipeline for Unicode normalization,
  hyphenation repair, whitespace cleanup, and document quality validation.

• Implemented context-aware recursive chunking with configurable overlap,
  metadata propagation, and chunk-level statistics for downstream semantic
  retrieval.


# ============================================================
# 22. IMMEDIATE NEXT STEP
# ============================================================

Do not optimize chunking further right now.

Current next step:

    Build the Embeddings module.

Recommended sequence:

    1. Understand embeddings conceptually.
    2. Choose an embedding model.
    3. Create src/embeddings/embedder.py.
    4. Generate embeddings for chunk text.
    5. Inspect vector dimensionality.
    6. Test semantic similarity.
    7. Validate batch embedding.
    8. Then move to ChromaDB/vector storage.

Current exact pipeline position:

    Ingestion      [COMPLETE]
        |
        v
    Cleaning       [COMPLETE V1]
        |
        v
    Chunking       [COMPLETE V1]
        |
        v
    Embeddings     [NEXT]
        |
        v
    Vector DB
        |
        v
    BM25
        |
        v
    Hybrid Retrieval
        |
        v
    Re-ranking
        |
        v
    Generation + Citations
        |
        v
    Evaluation