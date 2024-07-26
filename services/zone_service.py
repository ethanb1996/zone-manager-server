import os
import pandas as pd

from models.zone import Zone, Zone_Details
from models.point import Point

FILENAME = r"data/zones.csv"
class Zone_Service:
    
    def read_zones() -> list[Zone]: 
        if os.path.exists(FILENAME):
            return pd.read_csv(FILENAME).to_dict(orient='records')
        return []

    def write_zones(zones: list[Zone]) -> None:
        df = pd.DataFrame(zones)
        df.to_csv(FILENAME, index=False)

    def create_zone(zone_details:Zone_Details) -> Zone:
        zones = Zone_Service.read_zones()
        zone_id = len(zones) + 1
        new_zone = {"id": zone_id, "name": zone_details.name, "points": zone_details.points}
        zones.append(new_zone)
        Zone_Service.write_zones(zones)
        return new_zone

    def delete_zone(zone_id: int) -> str | None:
        zones = Zone_Service.read_zones()
        for zone in zones:
            if zone['id'] == zone_id:
                zones.remove(zone)
                Zone_Service.write_zones(zones)
                return f"Zone with id {zone_id} deleted"
        return None

    def get_all_zones() -> list[Zone]:
        return Zone_Service.read_zones()