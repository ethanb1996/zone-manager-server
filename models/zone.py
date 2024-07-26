from pydantic import BaseModel

class Zone_Details(BaseModel):
    name:str
    points: list[list[float]]

class Zone(BaseModel):
    id: int
    zone_detail:Zone_Details