
from pathlib import Path
from langchain_community.document_loaders import BSHTMLLoader


def load_html(file_path: Path):
    """Process all HTML files in a directory"""


  
    loader = BSHTMLLoader(str(file_path))
    documents = loader.load()

     # Add source information to metadata
    for doc in documents:
        doc.metadata['filename'] = file_path.name
        doc.metadata['source'] = str(file_path)
        doc.metadata['file_type'] = "html"

    return documents

       