import uuid
from typing import Dict

# Simple in-memory store for document snippets.
# Keyed by unique UUID string, value is document text.
DOCUMENT_REFERENCES: Dict[str, str] = {}

def store_document(content: str) -> str:
    """Store a document snippet and return its reference id."""
    ref_id = str(uuid.uuid4())
    DOCUMENT_REFERENCES[ref_id] = content
    return ref_id

def get_document(ref_id: str) -> str | None:
    """Retrieve a document snippet by reference id."""
    return DOCUMENT_REFERENCES.get(ref_id)
