from typing import Optional

from pydantic.main import BaseModel


class TableMetadata(BaseModel):
    uid: str
    page_id: Optional[int] = None
    is_inserted: Optional[bool] = None
