from pydantic.main import BaseModel


class Annotation(BaseModel):
    """
    The piece of information about the text line: it’s appearance or links to another document object.
    For example Annotation(1, 13, “italic”, “True”) says that text between 1st and 13th symbol was written in italic.

    url: https://dedoc.readthedocs.io/en/latest/dedoc_api_usage/api_schema.html#dedoc.api.schema.Annotation
    """

    start: int
    end: int
    name: str
    value: str
