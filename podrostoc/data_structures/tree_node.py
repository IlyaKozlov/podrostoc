from typing import List

from pydantic.main import BaseModel

from data_structures.line_metadata import LineMetadata
from podrostoc.data_structures.annotation import Annotation


class TreeNode(BaseModel):
    """
    Helps to represent document as recursive tree structure.
    It has list of children TreeNode nodes (empty list for a leaf node).

    url: https://dedoc.readthedocs.io/en/latest/dedoc_api_usage/api_schema.html#dedoc.api.schema.TreeNode
    """

    node_id: str
    text: str
    annotations: List[Annotation]
    metadata: LineMetadata
    subparagraphs: List["TreeNode"]
