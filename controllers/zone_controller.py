from fastapi import HTTPException

from models.zone import Zone
from models.point import Point
from services.zone_service import Zone_Service


class Zone_Controller:
    
    def create_zone(name:str, points:list[Point]) -> Zone:
        return Zone_Service.create_zone(name,points)
    
    def delete_zone(id:int) -> None:
        result = Zone_Service.delete_zone(id)
        if not result:
            raise HTTPException(status_code=404, detail="Zone not found")
        return result
    
    def fetch_zones() -> list[Zone]:
        return Zone_Service.get_all_zones()