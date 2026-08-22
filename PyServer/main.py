from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from src.routes import router as video_router
from fastapi.middleware.cors import CORSMiddleware

config = dotenv_values(".env")

app = FastAPI()

origins = [
    "http://localhost/:3000",
    "http://localhost/:8000",
    "http://159.2.5.43:3000"
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

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/test")
async def root():
    print("yes")
    return "yes"

app.include_router(video_router, tags=["videos"], prefix="/video")

# Implement ability to change what playlist by Video ID by naming DB_NAME the Video ID