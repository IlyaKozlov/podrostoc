from typing import Optional

from pydantic import BaseModel


class LineMetadata(BaseModel):
    """
    Holds information about document node/line metadata, such as page number or line type.

    url: https://dedoc.readthedocs.io/en/latest/dedoc_api_usage/api_schema.html#dedoc.api.schema.LineMetadata
    """

    paragraph_type: str
    page_id: int
    line_id: Optional[int]
