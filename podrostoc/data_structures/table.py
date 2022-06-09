from typing import List

from pydantic.main import BaseModel

from podrostoc.data_structures.table_metadata import TableMetadata


class Table(BaseModel):
    cells: List[List[str]]
    metadata: TableMetadata
