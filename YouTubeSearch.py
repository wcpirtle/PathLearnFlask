import googleapiclient.discovery
import googleapiclient.errors

import json

import config

def getTop5Videos(searchterm):

    api_service_name = "youtube"
    api_version = "v3"
    

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=config.api_key)

    request = youtube.search().list(
        part="snippet",
        maxResults=5,
        order="viewCount",
        q=searchterm,
        type="video",
    )

    response = request.execute()

    videoIds = {
        "videos":[
            {"id": response["items"][0]["id"]["videoId"]},
            {"id": response["items"][1]["id"]["videoId"]},
            {"id": response["items"][2]["id"]["videoId"]},
            {"id": response["items"][3]["id"]["videoId"]},
            {"id": response["items"][4]["id"]["videoId"]}
        ]
    }

    return videoIds