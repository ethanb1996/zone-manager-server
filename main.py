import os
import pandas as pd
from fastapi import FastAPI
from services.config_service import Config
from fastapi.middleware.cors import CORSMiddleware

Config.init()


from routes.zone_route import zone_router



FILENAME = Config.get_app_config()['FILENAME']
COLUMNS = Config.get_app_config()['COLUMNS']
ORIGINS = Config.get_app_config()['ORIGINS']
ALLOW_METHODS = Config.get_app_config()['ALLOW_METHODS']

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=ALLOW_METHODS,
    allow_headers=["*"],
)

app.include_router(zone_router)

def create_csv_file():
    df = pd.DataFrame(columns=COLUMNS)
    df.to_csv(FILENAME, index=False)
    print("CSV file with headers created successfully.")
    
if __name__ == "__main__":
    Config.init()
    if not os.path.exists(FILENAME):
        create_csv_file()
        
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
