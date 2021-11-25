from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Any
from ytmusicapi import YTMusic

api = FastAPI()
api_version = "0.0.1-beta"

# ---- Objects:

class YtId(BaseModel):
    """The id object contains information that can be used to uniquely identify the resource"""
    videoId: str = None
    playlistId: str = None

class YtSnippet(BaseModel):
    """The snippet object contains basic details about a search result, such as its title or description"""
    title: str = None
    description: str = None
    channelId: str = None
    channelTitle: str = None

class YtResource(BaseModel):
    """Item of search result. Compare: https://developers.google.com/youtube/v3/docs/search#resource"""
    id: YtId = None
    snippet: YtSnippet = None

class YtItems(BaseModel):
    """Result of API search request"""
    items: List[YtResource]

# ---- Endpoints:

@api.get("/")
def hello_world():
    return {"server": "YT-Music Search Microservice", "version": api_version}

@api.get("/search")
def search(q: str = None, maxResults: int = 3):
    if q is not None:
        # search
        ytmusic = YTMusic() # With auth.: YTMusic('headers_auth.json')
        # Ref.: https://ytmusicapi.readthedocs.io/en/latest/reference.html
        search_results = ytmusic.search(query = q, limit = maxResults, filter = None)
        if search_results is not None and len(search_results) > 0:
            items = []
            for result in search_results:
                # print(result["resultType"])
                if len(items) >= maxResults:
                    # Note: limit doesn't seem to work so we abort manually (version from: 2021.11.25)
                    break
                # add result with Youtube Data API compatible format
                yt_id = YtId(videoId = result.get("videoId"))
                yt_snippet = YtSnippet(title = result.get("title"), description = result.get("resultType"))
                yt_resource = YtResource(id = yt_id, snippet = yt_snippet)
                items.append(yt_resource)
            return YtItems(items = items)
        else:
            yt_items = YtItems(items = [])
            return yt_items
    else:
        raise HTTPException(status_code=400, detail="Missing query parameter 'q'")
