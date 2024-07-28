from fastapi import APIRouter

from models.zone import Zone, Zone_Details
from controllers.zone_controller import Zone_Controller

zone_router = APIRouter()

Zone_Controller.get_avalaible_ids()

@zone_router.post("/create_zone", response_model=Zone)
def create_zone(zone_detail:Zone_Details):
    return Zone_Controller.create_zone(zone_detail) 

@zone_router.delete("/delete_zone/{id}", response_model=str)
def delete_zone(id: int):
    return Zone_Controller.delete_zone(id)

@zone_router.get("/all_zones", response_model=list[Zone])
def fetch_zones():
    return Zone_Controller.fetch_zones()

