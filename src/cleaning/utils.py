
#this is the utils file for cleaning module. It contains utility functions that are used in the cleaning module.

import re
import unicodedata

def normalize_unicode(text: str) -> str:
    """Normalize unicde characters."""

    return unicodedata.normalize("NFKC", text)

def repair_hyphenation(text: str) -> str:
    """Repair words broken across lines."""

    return re.sub(r"(\w)-\n(\w)", r"\1\2", text)

def collapse_spaces(text: str) -> str:
    """Replace multiple spaces/tabs with one space."""

    return re.sub(r"[ \t]+", " ", text)

def collapse_blank_lines(text: str) -> str:
    """Replace 3+ blank lines with two."""

    return re.sub(r"\n{3,}", "\n\n", text)

def remove_trailing_spaces(text: str) -> str:
    """Remove trailing spaces from every line."""

    lines = [line.rstrip() for line in text.splitlines()]
    return "\n".join(lines)