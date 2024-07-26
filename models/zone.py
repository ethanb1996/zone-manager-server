from pydantic import BaseModel

class Zone_Details(BaseModel):
    name:str
    points: list[list[float]]

class Zone(Zone_Details):
    id: int