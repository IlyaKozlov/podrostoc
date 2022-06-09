from typing import List

from pydantic.main import BaseModel

from podrostoc.data_structures.table import Table
from podrostoc.data_structures.tree_node import TreeNode


class DocumentContent(BaseModel):
    tables: List[Table]
    structure: TreeNode
