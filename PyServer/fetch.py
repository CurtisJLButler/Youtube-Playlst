import requests
import json
import time

async def fetch_data():
    # Example API
    print("Fetching")
    params = {
    "part": "snippet,contentDetails",
    "maxResults": "50",
    "playlistId": "PLflBssihv_O9-p25fni3Jt8eTMHQf62y4",
    "key": ""
    }
    url = "https://www.googleapis.com/youtube/v3/playlistItems"
    

    allVideos = []
    nextPageToken = ""
    stopat = 1

    while(True):
        if nextPageToken:
            params["pageToken"] = nextPageToken

        params["cache_buster"] = str(time.time())
        res = requests.get(url, params={
            "part": "snippet,contentDetails",
            "maxResults": "50",
            # "playlistId": "PLflBssihv_O_QnsAFSpxOO8RAfaV2KIVc", # Test
            "playlistId": "PLflBssihv_O9-p25fni3Jt8eTMHQf62y4", # Final
            "key": "",
            "pageToken": nextPageToken
        })
        response = json.loads(res.text)
        items = response.get("items", [])
        for item in items:
            video = {
                "thumbnail": item["snippet"]["thumbnails"].get("default", {}).get("url"),
                "title": item["snippet"]["title"],
                "description": item["snippet"]["description"],
                "video_id": item["contentDetails"]["videoId"],
                "playlist_id": "PLflBssihv_O9-p25fni3Jt8eTMHQf62y4"

                
            }
            if(video["description"] == ""):
                video["description"] = "No description"
            if not video["thumbnail"]:
                video["thumbnail"] = "img/thumb.jpg"
            
            allVideos.append(video)
        nextPageToken = response.get("nextPageToken")
        stopat -= 1
        if(nextPageToken):
           continue
        else:
            break
        
    return allVideos
