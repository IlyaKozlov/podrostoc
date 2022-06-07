from typing import List

from pydantic.main import BaseModel

from data_structures.table import Table
from data_structures.tree_node import TreeNode


class DocumentContent(BaseModel):
    tables: List[Table]
    structure: TreeNode
