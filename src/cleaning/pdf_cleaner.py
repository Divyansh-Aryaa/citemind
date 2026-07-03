
# This is responsible for cleaning the PDF data after INGESTION and then send it further down the pipline for RETRIEVAL and PREDICTION

from langchain_core.documents import Document

from src.cleaning.utils import (
    normalize_unicode,
    repair_hyphenation,
    collapse_spaces,
    collapse_blank_lines,
    remove_trailing_spaces,
)

def clean_pdf(doc: Document) -> Document:
    """Clean a PDF document."""

    text = doc.page_content

    text = normalize_unicode(text)
    text = repair_hyphenation(text)

    text = text.strip()
    text = collapse_spaces(text)
    text = collapse_blank_lines(text)
    text = remove_trailing_spaces(text)

    return Document(
        page_content = text,
        metadata = doc.metadata.copy() # keeping a copy of the Metadata, not directly changing the original file, keeping an option for fall back if anything goes wrong.

    )


