
#This file is the main file that is responsible for redirecting the cleaning of the documents to the respective cleaning files based on the file type.

from langchain_core.documents import Document

from src.cleaning.pdf_cleaner import clean_pdf
from src.cleaning.html_cleaner import clean_html

def clean_documents(documents: list[Document]) -> list[Document]:
    """Clean all the loaded Documents."""

    cleaned_documents = []

    for doc in documents:

        file_type = doc.metadata.get("file_type")

        if file_type == "pdf":
            cleaned_doc = clean_pdf(doc)

        elif file_type == "html":
            cleaned_doc = clean_html(doc)
        
        else:
            #markdown and text 
            cleaned_doc = clean_html(doc)
        
        cleaned_documents.append(cleaned_doc)


    return cleaned_documents

        
if __name__ == "__main__":
     
     from pathlib import Path
     from src.ingestion.loader import load_documents

     PROJECT_ROOT = Path(__file__).reslove().parents[2]
     DATA_DIR = PROJECT_ROOT / "data" / "raw" 

     docs, stats = load_documents(DATA_DIR)

     cleaned_docs = clean_documents(docs)

     print("=" * 60)
     print("CLEANING REPORT")
     print("=" * 60)

     print(f"Original Length : {len(docs[0].page_content)}")
     print(f"Cleaned Lenght : {len(cleaned_docs[0].page_content)}")
     print(f"Characters Removed : {len(docs[0].page_content)} - {len(cleaned_docs[0].page_content)}")
