from fastapi import APIRouter

from models.zone import Zone
from models.point import Point
from controllers.zone_controller import Zone_Controller

zone_router = APIRouter()

@zone_router.post("/zone", response_model=Zone)
def create_zone(name:str,points: list[Point]):
    return Zone_Controller.create_zone(name,points) 

@zone_router.delete("/zone/{id}", response_model=str)
def delete_zone(id: int):
    return Zone_Controller.delete_zone(id)

@zone_router.get("/all_zones", response_model=list[Zone])
def fetch_zones():
    return Zone_Controller.fetch_zones()

