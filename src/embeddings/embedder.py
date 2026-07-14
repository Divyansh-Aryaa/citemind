# this file is responsible for embedding the text chunks into vector representations using sentence-transformers/all-MiniLM-L6-v2 embedding model.

from pathlib import Path

from langchain_core.documents import Document
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim


from src.ingestion.loader import load_documents
from src.cleaning.cleaner import clean_documents
from src.chunking.splitter import split_documents


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def load_embedding_model() -> SentenceTransformer:

    """Load and return the sentence-transformer embedding model."""

    return SentenceTransformer(MODEL_NAME)

def embed_documents(
        documents: list[Document],
        model: SentenceTransformer,
):
    """Convert document chunks into dense numerical embeddings.
    
    Args:
        documents:
            List of chunked Langchain Document objects.
            
            model:
                Loaded SentenceTransformer embedding model.
                
    Returns:
        Numerical embeddings for all document chunks
    
    """

    texts = [doc.page_content for doc in documents]

    embeddings = model.encode(
            texts,
            batch_size = 32,
            show_progress_bar = True,
            normalize_embeddings = True,
        )
    return embeddings 


if __name__ == "__main__":

    PROJECT_ROOT = Path(__file__).resolve().parents[2]
    DATA_DIR = PROJECT_ROOT / "data" / "raw"

    #Step 1: Ingestion

    docs, stats = load_documents(DATA_DIR)

    #Step 2: Cleaning
    cleaned_docs = clean_documents(docs)

    #Step 3: Chunking
    chunks = split_documents(cleaned_docs)

    #Step 4: Load embedding model 
    model = load_embedding_model()

    #Step 5: Generate embeddings
    embeddings = embed_documents(chunks, model)
    

    print("\n" + "=" * 60)
    print("EMBEDDING SUMMARY")
    print("=" * 60)

    print(f"Total Chunks       : {len(chunks)}")
    print(f"Total Embeddings   : {len(embeddings)}")
    print(f"Embedding Dimension: {embeddings.shape[1]}")
    print(f"Embedding Shape    : {embeddings.shape}")

    print("\nEmbedding generation completed successfully.\n")
