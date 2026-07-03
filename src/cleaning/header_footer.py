
#this file is responsible to clean the the repeated header and footer in the documents. 

from collections import defaultdict
from langchain_core.documents import Document

def group_by_source(documents: list[Document]):
    """Group pages belonging to the same source document."""

    groups = defaultdict(list)

    for doc in documents:

        source = doc.metadata["source"]

        groups[source].append(doc)

    return groups

def first_non_empty_lines(doc: Document, n: int = 3) -> list[str]:
    """Return the first n non-empty lines from a page."""

    lines = []

    for line in doc.page_content.splitlines():
        line = line.strip()

        if line:
            lines.append(line)

        if len(lines) == n:
            break

    return lines

