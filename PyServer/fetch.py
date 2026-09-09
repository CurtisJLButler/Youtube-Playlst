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
    "key": "AIzaSyAYZn4_c-Dfl9KmZdfEPEsz0SlkpvLt9EU"
    }
    url = "https://www.googleapis.com/youtube/v3/playlistItems"
    

    allVideos = []
    nextPageToken = ""
    stopat = 1


    while(stopat):
        if nextPageToken:
            params["pageToken"] = nextPageToken

        params["cache_buster"] = str(time.time())
        res = requests.get(url, params={
            "part": "snippet,contentDetails",
            "maxResults": "50",
            # "playlistId": "PLflBssihv_O_QnsAFSpxOO8RAfaV2KIVc", # Test
            "playlistId": "PLflBssihv_O9-p25fni3Jt8eTMHQf62y4", # Final
            "key": "AIzaSyAYZn4_c-Dfl9KmZdfEPEsz0SlkpvLt9EU",
            "pageToken": nextPageToken
        })
        response = json.loads(res.text)
        items = response.get("items", [])
        for item in items:
            if(item["snippet"]["thumbnails"].get("maxres", {}).get("url") != None):
                thumbnail = item["snippet"]["thumbnails"].get("maxres", {}).get("url")
                print(thumbnail)
            elif(item["snippet"]["thumbnails"].get("medium", {}).get("url") != None):
                thumbnail = item["snippet"]["thumbnails"].get("medium", {}).get("url")
            else:
                thumbnail = item["snippet"]["thumbnails"].get("default", {}).get("url")

                 
            video = {
                "thumbnail": thumbnail,
                "title": item["snippet"]["title"],
                "description": item["snippet"]["description"],
                "video_id": item["contentDetails"]["videoId"],
                "playlist_id": "PLflBssihv_O9-p25fni3Jt8eTMHQf62y4",
                "descState": "hidden",
                "showHide": "Show description"

                
            }
            if(video["title"] == "Deleted video" or video["title"] == "Private video"):
                video["thumbnail"] = "http://localhost:8000/noimage"
                video["description"] = 0
            if(video["description"] == ""):
                video["description"] = 0
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
