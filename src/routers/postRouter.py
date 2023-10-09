from fastapi import APIRouter, HTTPException
from src.client.cockroach import CockroachDBClient
import json


class postRouter():
    def __init__(self, client: CockroachDBClient):
        from src.db.postHandler import get_All_Post, get_single_Post, add_Post
        self._ENDPOINT_GET_ALL_POST = "/get_all_post/"
        self._ENDPOINT_GET_SINGLE_POST = "/get_single_post/"
        self._ENDPOINT_ADD_POST = "/add_post/"
        self._client = client
        self._router = APIRouter(prefix="/post")

        @self._router.post(self._ENDPOINT_GET_ALL_POST)
        async def route_getallpostPOST():
            return json.dumps(get_All_Post(self._client.get_session()))

        @self._router.get(self._ENDPOINT_GET_ALL_POST)
        async def route_getallpostGET():
            return json.dumps(get_All_Post(self._client.get_session()))

        @self._router.post(self._ENDPOINT_GET_SINGLE_POST)
        async def route_getsinglepostPOST(pid: str):
            if not pid:
                raise HTTPException(status_code=400, detail="Invalid input data")
            return json.dumps(get_single_Post(self._client.get_session(), pid))

        @self._router.get(self._ENDPOINT_GET_SINGLE_POST)
        async def route_getsinglepostGET(pid: str):
            if not pid:
                raise HTTPException(status_code=400, detail="Invalid input data")
            return json.dumps(get_single_Post(self._client.get_session(), pid))

        @self._router.post(self._ENDPOINT_ADD_POST)
        async def route_addpostPOST(title: str, body: str, author_name: str, author_id: str):
            if not title or not body or not author_name or not author_id:
                raise HTTPException(status_code=400, detail="Invalid input data")
            return json.dumps(add_Post(self._client.get_session(), title, body, author_name, author_id))

        @self._router.get(self._ENDPOINT_ADD_POST)
        async def route_addpostGET(title: str, body: str, author_name: str, author_id: str):
            if not title or not body or not author_name or not author_id:
                raise HTTPException(status_code=400, detail="Invalid input data")
            return json.dumps(add_Post(self._client.get_session(), title, body, author_name, author_id))

    @property
    def get_Router(self):
        return self._router
