from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    year: int
    price: float