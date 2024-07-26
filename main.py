import os
import pandas as pd
from fastapi import FastAPI

from routes.zone_route import zone_router

FILENAME = r"data/zones.csv"
COLUMNS = ['id', 'name', 'points']

app = FastAPI()

app.include_router(zone_router)

def create_csv_file():
    df = pd.DataFrame(columns=COLUMNS)
    df.to_csv(FILENAME, index=False)
    print("CSV file with headers created successfully.")
    
if __name__ == "__main__":
    if not os.path.exists(FILENAME):
        create_csv_file()
        
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
