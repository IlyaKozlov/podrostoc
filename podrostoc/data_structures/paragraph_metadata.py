from typing import Dict, Optional

from pydantic.main import BaseModel


class ParagraphMetadata(BaseModel):
    paragraph_type: str
    predicted_classes: Optional[Dict[str, float]] = None
    page_id: Optional[int] = None
    line_id: Optional[int] = None
