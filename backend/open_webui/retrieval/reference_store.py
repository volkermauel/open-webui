import uuid
from typing import Dict

# Simple in-memory store for document snippets.
# Keyed by unique UUID string, value is document text.
DOCUMENT_REFERENCES: Dict[str, str] = {}
# Store full citation/source lists referenced by id
CITATION_REFERENCES: Dict[str, list] = {}


def store_document(content: str) -> str:
    """Store a document snippet and return its reference id."""
    ref_id = str(uuid.uuid4())
    DOCUMENT_REFERENCES[ref_id] = content
    return ref_id


def get_document(ref_id: str) -> str | None:
    """Retrieve a document snippet by reference id."""
    return DOCUMENT_REFERENCES.get(ref_id)


def store_sources(sources: list) -> str:
    """Store a list of sources/citations and return its reference id."""
    ref_id = str(uuid.uuid4())
    CITATION_REFERENCES[ref_id] = sources
    return ref_id


def get_sources(ref_id: str) -> list | None:
    """Retrieve stored sources/citations by reference id."""
    return CITATION_REFERENCES.get(ref_id)
