"""
text_cleaning.py
----------------
Utility functions for text preprocessing and postprocessing.
"""

ACRONYM_MAP = {
    "fyi": "for your information",
    "asap": "as soon as possible",
    "idk": "I don't know",
    # add more acronyms here
}

def expand_acronyms(text: str) -> str:
    """Expand common acronyms in text."""
    words = text.split()
    expanded = [ACRONYM_MAP.get(w.lower(), w) for w in words]
    return " ".join(expanded)


def basic_cleanup(text: str) -> str:
    """Basic cleanup (strip extra spaces, normalize case, etc.)."""
    return " ".join(text.strip().split())
