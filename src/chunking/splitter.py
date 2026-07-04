
#this file is responsible for splitting the text into chunks based on the specified chunk size and overlap. 

from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.ingestion.loader import load_documents
from src.cleaning.cleaner import clean_documents

CHUNK_SIZE = 700
CHUNK_OVERLAP = 100

def create_text_splitter():
    return RecursiveCharacterTextSplitter(
        chunk_size = CHUNK_SIZE,
        chunk_overlap = CHUNK_OVERLAP,
        length_function = len,
    )

def split_documents(documents: list[Document]) -> list[Document]:
    """Split cleaned documents into overlap chunks.
    
    Args:
        documents:
            List of cleaned LangChain Documents.

    Returns:
        list[Document]: List of chunked Documents.
    
    """

    splitter = create_text_splitter()
    return splitter.split_documents(documents)



if __name__ == "__main__":

    PROJECT_ROOT = Path(__file__).resolve().parents[2]
    DATA_DIR = PROJECT_ROOT / "data" / "raw"

    docs, stats = load_documents(DATA_DIR)

    cleaned_docs = clean_documents(docs)

    chunks = split_documents(cleaned_docs)

    print("=" * 60)
    print("CHUNKING SUMMARY")
    print("=" * 60)

    print(f"Original Documents   : {len(cleaned_docs)}")
    print(f"Total Chunks         : {len(chunks)}")
    print(f"Average Chunk Size   : {sum(len(chunk.page_content) for chunk in chunks) / len(chunks):.2f} characters")
    print(f"Largest Chunk        : {max(len(chunk.page_content) for chunk in chunks)} characters")
    print(f"Smallest Chunk       : {min(len(chunk.page_content) for chunk in chunks)} characters")
    print(f"Average Chunk/Doc    : {len(chunks) / len(cleaned_docs):.2f}")

    print("\nChunking completed successfully.\n")
