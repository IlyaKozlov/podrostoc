from typing import List

from pydantic.main import BaseModel

from data_structures.cell_with_meta import CellWithMeta
from podrostoc.data_structures.table_metadata import TableMetadata


class Table(BaseModel):
    """
    Holds information about tables in the document.
    We assume that a table has rectangle form (has the same number of columns in each row).
    Table representation is row-based i.e. external list contains list of rows.

    url: https://dedoc.readthedocs.io/en/latest/dedoc_api_usage/api_schema.html#dedoc.api.schema.Table
    """

    cells: List[List[CellWithMeta]]
    metadata: TableMetadata
