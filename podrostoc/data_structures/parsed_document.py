from typing import List, Optional

from pydantic import BaseModel

from podrostoc.data_structures.document_content import DocumentContent
from podrostoc.data_structures.document_metadata import DocumentMetadata


class ParsedDocument(BaseModel):
    version: str
    warnings: List[str]
    metadata: DocumentMetadata
    content: DocumentContent
    attachments: Optional[List['ParsedDocument']] = None
