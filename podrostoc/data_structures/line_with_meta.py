from typing import List

from pydantic import BaseModel

from data_structures.annotation import Annotation


class LineWithMeta(BaseModel):
    """
    Textual line with text annotations.

    url: https://dedoc.readthedocs.io/en/latest/dedoc_api_usage/api_schema.html#dedoc.api.schema.LineWithMeta
    """

    text: str
    annotations: List[Annotation]
