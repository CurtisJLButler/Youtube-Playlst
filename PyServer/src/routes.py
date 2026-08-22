from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from src.scripts.updatePlaylist import update as newvideo

from src.models import Video, VideoUpdate
from src.scripts.fetch import fetch_data as grab

router = APIRouter()


@router.post("/", response_description="Add video to playlist", status_code=status.HTTP_201_CREATED, response_model=Video)
def create_book(request: Request, video: Video = Body(...)):
    video = jsonable_encoder(video)
    new_video = request.app.database["videos"].insert_one(video)
    created_video = request.app.database["videos"].find_one(
        {"_id": new_video.inserted_id}
    )

    return created_video

@router.post("/new", response_description="Add video to playlist", status_code=status.HTTP_201_CREATED, response_model=Video)
async def create_book(request: Request, video: Video = Body(...)):
    video = jsonable_encoder(video)
    playlist = await grab()
    created_video = newvideo(playlist, request)
    return created_video


@router.get("/", response_description="List all videos", response_model=List[Video])
def list_videos(request: Request):
    print("fetching")
    videos = list(request.app.database["videos"].find())
    return videos



@router.get("/{id}", response_description="Get a single video by id", response_model=Video)
def find_book(id: int, request: Request):
    if (video := request.app.database["videos"].find_one({"_id": id})) is not None:
        return video
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Video with ID {id} not found")



@router.put("/{id}", response_description="Update a video", response_model=Video)
def update_video(id: int, request: Request, video: VideoUpdate = Body(...)):
    video = {k: v for k, v in video.dict().items() if v is not None}
    if len(video) >= 1:
        update_result = request.app.database["videos"].update_one({"_id": id}, {"$set": video})

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Video with ID {id} not found")

    if (
        existing_video := request.app.database["videos"].find_one({"_id": id})
    ) is not None:
        return existing_video

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Video with ID {id} not found")



@router.delete("/{id}", response_description="Delete a video")
def delete_video(id: int, request: Request, response: Response):
    delete_result = request.app.database["videos"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Video with ID {id} not found")