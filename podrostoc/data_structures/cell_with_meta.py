from typing import List

from pydantic import BaseModel

from data_structures.line_with_meta import LineWithMeta


class CellWithMeta(BaseModel):
    """
    Holds the information about the cell: list of lines and cell properties (rowspan, colspan, invisible).

    url: https://dedoc.readthedocs.io/en/latest/dedoc_api_usage/api_schema.html#dedoc.api.schema.CellWithMeta
    """

    # TODO add descriptions
    lines: List[LineWithMeta]
    rowspan: int
    colspan: int
    invisible: bool
