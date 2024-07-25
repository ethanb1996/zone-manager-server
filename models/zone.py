from pydantic import BaseModel

from point import Point

class Zone(BaseModel):
    id: int
    name:str
    points: list[Point]