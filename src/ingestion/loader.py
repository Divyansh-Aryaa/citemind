"""this module contains functions to load documents from a directory."""

from pathlib import Path
from src.ingestion.pdf_loader import load_pdf
from src.ingestion.markdown_loader import load_markdown
from src.ingestion.html_loader import load_html
from src.ingestion.text_loader import load_text

SUPPORTED_LOADERS = {

    ".pdf": load_pdf,

    ".md": load_markdown,

    ".txt": load_text,

    ".html": load_html,
}

def load_documents(directory):
    """Load documents from a directory.

    Args:
        directory (str or Path): Path to the directory containing documents.
    
        
    Returns:
        list[Document]: A list of LangChain Document objects.   

    """

    stats = {
    "pdf": 0,
    "markdown": 0,
    "text": 0,
    "html": 0,
    }

    directory = Path(directory)

    all_documents = []

    for file in directory.rglob("*"):

        if not file.is_file():
            continue

        extension = file.suffix.lower()

        loader = SUPPORTED_LOADERS.get(extension)

        if file.name.startswith("."):
            continue

        if loader is None:
            print(f"\n ⚠ Unsupported file type:  {file.name}\n")

            continue

        print(f" 📂 Loading.......{file.name}")

        docs = loader(file)

        if extension == ".pdf":
            stats["pdf"] += 1
        elif extension == ".md":
            stats["markdown"] += 1
        elif extension == ".html":
            stats["html"] += 1
        else:
            stats["text"] += 1

        print(f"Loaded {len(docs)} documents")
        all_documents.extend(docs)

        ##print(f"\nTotal Documents Loaded: {len(all_documents)}")

    return all_documents, stats


if __name__ == "__main__":

    PROJECT_ROOT = Path(__file__).resolve().parents[2]

    DATA_DIR = PROJECT_ROOT / "data" / "raw"

    documents, stats = load_documents(DATA_DIR)

    print("\n" + "=" * 60)
    print("INGESTION SUMMARY")
    print("=" * 60)

    if documents:
        print(f"\nPDF Files Loaded: {stats['pdf']}")
        print(f"\nMarkdown Files Loaded: {stats['markdown']}")
        print(f"\nText Files Loaded: {stats['text']}")
        print(f"\nHTML Files Loaded: {stats['html']}")
        print("\n" + "-" * 60)
        print(f"Total Documents Loaded: {len(documents)}")



