from pydantic.main import BaseModel


class Annotation(BaseModel):
    start: int
    end: int
    name: str
    value: str
