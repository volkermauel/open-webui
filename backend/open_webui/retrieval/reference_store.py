import uuid
from typing import Dict

# Simple in-memory store for document snippets.
# Keyed by unique UUID string, value is document text.
DOCUMENT_REFERENCES: Dict[str, str] = {}
# Store complete citation data separately so only a reference ID needs to be
# sent with chat responses.
CITATION_REFERENCES: Dict[str, list] = {}



def store_document(content: str) -> str:
    """Store a document snippet and return its reference id."""
    ref_id = str(uuid.uuid4())
    DOCUMENT_REFERENCES[ref_id] = content
    return ref_id



def get_document(ref_id: str) -> str | None:
    """Retrieve a document snippet by reference id."""
    return DOCUMENT_REFERENCES.get(ref_id)


def store_citations(citations: list) -> str:
    """Store a list of citations and return its reference id."""
    ref_id = str(uuid.uuid4())
    CITATION_REFERENCES[ref_id] = citations
    return ref_id


def get_citations(ref_id: str) -> list | None:
    """Retrieve citations by reference id."""
    return CITATION_REFERENCES.get(ref_id)

def get_document(ref_id: str) -> str | None:
    """Retrieve a document snippet by reference id."""
    return DOCUMENT_REFERENCES.get(ref_id)

