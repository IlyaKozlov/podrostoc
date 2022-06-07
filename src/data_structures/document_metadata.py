from typing import Optional

from pydantic.main import BaseModel


class DocumentMetadata(BaseModel):
    uid: str
    file_name: str
    size: int
    modified_time: int
    created_time: int
    access_time: int
    file_type: Optional[str]
    other_fields: Optional[dict]
