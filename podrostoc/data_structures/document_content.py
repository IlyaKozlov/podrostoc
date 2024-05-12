from typing import List

from pydantic import BaseModel, Field

from podrostoc.data_structures.table import Table
from podrostoc.data_structures.tree_node import TreeNode


class DocumentContent(BaseModel):
    """Content of the document - structured text and tables.

    url: https://dedoc.readthedocs.io/en/latest/dedoc_api_usage/api_schema.html#dedoc.api.schema.DocumentContent
    """

    tables: List[Table] = Field(description="Tables from the document.")
    structure: TreeNode = Field(
        description="Text of the document, organized in a tree."
    )
