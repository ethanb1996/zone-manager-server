import os
import pandas as pd

from models.zone import Zone, Zone_Details

FILENAME = r"data/zones.csv"
COLUMNS = ['id', 'name', 'points']

class Zone_Service:
    
    def read_zones() -> list[Zone]: 
        if os.path.exists(FILENAME):
            zones_dict = pd.read_csv(FILENAME).to_dict(orient='records')
            return [Zone(id=z['id'],name=z['name'],points=eval(z['points'])) for z in zones_dict]
        return []

    def write_zones(zones: list[Zone]) -> None:
        dict_list = [zone.model_dump() for zone in zones]
        df = pd.DataFrame(dict_list,columns=COLUMNS)
        df.to_csv(FILENAME, index=False)

    def create_zone(zone_details:Zone_Details) -> Zone:
        zones = Zone_Service.read_zones()
        zone_id = len(zones) + 1
        new_zone = Zone(id=zone_id, **zone_details.model_dump())
        zones.append(new_zone)
        Zone_Service.write_zones(zones)
        return new_zone

    def delete_zone(zone_id: int) -> str | None:
        zones = Zone_Service.read_zones()
        for zone in zones:
            if zone.id == zone_id:
                zones.remove(zone)
                Zone_Service.write_zones(zones)
                return f"Zone with id {zone_id} deleted"
        return None

    def get_all_zones() -> list[Zone]:
        return Zone_Service.read_zones()