"""Module for loading Markdown files and converting them into LangChain Document objects."""

from pathlib import Path
from langchain_core.documents import Document


def load_markdown(file_path: Path):
    """Load a single Markdown file and convert it into
      a LangChain Document object while preserving useful 
      metadata.

      Args:
        file_path (Path): Path to the Markdown file.
        
      Returns:
        list[Document]: A list containing one LangChain Document.

    """

    with open(file_path, "r", encoding ="utf-8") as f:
        text = f.read()

    document = Document(
        page_content = text,
        metadata = {
            "source": str(file_path),
            "filename": file_path.name,
            "file_type": "markdown"
        }
    )
    return [document]
