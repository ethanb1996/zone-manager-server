import os
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.zone_route import zone_router

FILENAME = r"data/zones.csv"
COLUMNS = ['id', 'name', 'points']
origins = [
    "http://localhost:4200",  # Or you can add more addresses 
]

# Add CORSMiddleware to the application

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
