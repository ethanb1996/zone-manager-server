from fastapi import APIRouter

from models.zone import Zone

zone_router = APIRouter()

@zone_router.post("/zone", response_model=Zone)
def create_zone(name:str,points: list[list[float]]):
    return

@zone_router.delete("/zone/{id}", response_model=str)
def delete_zone(id: int):
    return

@zone_router.get("/all_zones", response_model=list[Zone])
def fetch_zones(name:str,points: list[list[float]]):
    return

