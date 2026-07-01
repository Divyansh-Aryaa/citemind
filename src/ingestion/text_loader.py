"""
text_loader.py

Loads a single text (.txt) file and converts it into a LangChain
Document object while preserving useful metadata.
"""

from pathlib import Path
from langchain_core.documents import Document

def load_text(file_path: Path):
    """
    Load a single text file.

    Args:
        file_path (Path): Path to the text file.

    Returns:
        list[Document]: A list containing one LangChain Document.
    """

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    document = Document(
        page_content = text,
        metadata={
            "source": str(file_path),
            "filename": file_path.name,
            "file_type": "text"
        }
    )
    return [document]
