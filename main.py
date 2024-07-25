from fastapi import FastAPI

from routes.zone_routes import zone_router

app = FastAPI()

app.include_router(zone_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
