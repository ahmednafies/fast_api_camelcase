from pydantic import BaseModel
from humps import camelize


def to_camel(string):
    return camelize(string)


class User(BaseModel):
    first_name: str
    last_name: str = None
    age: float

    class Config:
        alias_generator = to_camel
