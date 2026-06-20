from fastapi import FastAPI
from fetch import fetch_data as fetch
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://192.168.2.10:8000",  # frontend origin
    "http://192.168.2.10:3000",  # optionally include this
    "http://curtisjlbutler.com:3000",
    "http://curtisjlbutler.com:8000",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # which origins are allowed to request
    allow_credentials=True,
    allow_methods=["*"],         # allow all methods GET, POST, etc
    allow_headers=["*"],         # allow all headers
)

@app.get("/")
async def root():
    list = await fetch(app.key)
    print(list)
    return {"videos": list}