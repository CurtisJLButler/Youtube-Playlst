from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router as video_router
from fetch import fetch_data as fetch
from fastapi.middleware.cors import CORSMiddleware

config = dotenv_values(".env")

app = FastAPI()

origins = [
    "http://192.168.2.10:8000",  # frontend origin
    "http://192.168.2.10:3000",  # optionally include this
    "http://curtisjlbutler.com:3000",
    "http://curtisjlbutler.com:8000",
    "http://localhost:8000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # which origins are allowed to request
    allow_credentials=True,
    allow_methods=["*"],         # allow all methods GET, POST, etc
    allow_headers=["*"],         # allow all headers
)

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    app.key = config["KEY"]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/test")
async def root():
    list = await fetch(config[app.key])
    print(list)
    return {"videos": list}

app.include_router(video_router, tags=["videos"], prefix="/video")

# Implement ability to change what playlist by Video ID by naming DB_NAME the Video ID