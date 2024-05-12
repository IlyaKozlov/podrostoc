from pydantic import BaseModel, Field


class DocumentMetadata(BaseModel):
    """
    Document metadata like its name, size, author, etc.

    url: https://dedoc.readthedocs.io/en/latest/dedoc_api_usage/api_schema.html#dedoc.api.schema.DocumentMetadata
    """

    uid: str = Field(description="document uid")
    file_name: str = Field(description="document file name")
    temporary_file_name: str  # TODO add the description
    size: int = Field(description="document size in bytes")
    modified_time: int = Field(
        description="last modification time in seconds since epoch"
    )
    created_time: int = Field(description="creation time in seconds since epoch")
    access_time: int = Field(description="creation time in seconds since epoch")
    file_type: str  # TODO add the description
