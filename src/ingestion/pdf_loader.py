
#this file will be resposible for loading the data and converting the raw data into a langchain Document object

from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader


def load_pdf(file_path: Path):
    """
    Load a single PDF file
    """

    loader = PyMuPDFLoader(str(file_path))
    documents = loader.load()
    # Add source information to metadata

    for doc in documents:
        doc.metadata['filename'] = file_path.name
        doc.metadata['source'] = str(file_path)
        doc.metadata['file_type'] = "pdf"

    return documents

 