from typing import List, Optional

from pydantic import BaseModel, Field

from podrostoc.data_structures.document_content import DocumentContent
from podrostoc.data_structures.document_metadata import DocumentMetadata


class ParsedDocument(BaseModel):
    """
    Response from the dedoc.

    url: https://dedoc.readthedocs.io/en/latest/dedoc_api_usage/api_schema.html#dedoc.api.schema.ParsedDocument
    """

    content: DocumentContent = Field(
        description="document content, such as text and tables"
    )
    metadata: DocumentMetadata = Field(
        description="document metadata such as creation date, modification date, etc."
    )
    version: str = Field(description="dedoc version")
    warnings: List[str] = Field(
        description="dedoc warnings, during the document handling"
    )
    attachments: Optional[List["ParsedDocument"]] = Field(
        default=None, description="ducument attachments, such as notes in the pdf file"
    )
