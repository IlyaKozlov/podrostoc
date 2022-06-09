from typing import List

from pydantic.main import BaseModel

from podrostoc.data_structures.annotation import Annotation
from podrostoc.data_structures.paragraph_metadata import ParagraphMetadata


class TreeNode(BaseModel):
    node_id: str
    text: str
    annotations: List[Annotation]
    metadata: ParagraphMetadata
    subparagraphs: List['TreeNode']
