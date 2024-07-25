import pandas as pd
import os
from models.zone import Zone

FILENAME = "/data/zones.csv"

def read_zones():
    if os.path(FILENAME):
        return pd.read_csv(FILENAME).to_dict(orient='records')
    return []
