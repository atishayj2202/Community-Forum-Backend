from fastapi import APIRouter, HTTPException
from src.client.cockroach import CockroachDBClient
import json

class userRouter():
    def __init__(self, client: CockroachDBClient):
        from src.db.userHandler import create_user, get_user
        self._ENDPOINT_GET_USER = "/get_user/"
        self._ENDPOINT_CREATE_USER = "/create_user/"
        self._client = client
        self._router = APIRouter(prefix="/user")

        @self._router.post(self._ENDPOINT_CREATE_USER)
        async def route_createuserPOST(name: str, uid: str):
            if not uid or not name:
                raise HTTPException(status_code=400, detail="Invalid input data")
            return json.dumps(create_user(self._client.get_session(), name, uid))

        @self._router.post(self._ENDPOINT_GET_USER)
        async def route_getuserPOST(id: str):
            if not id:
                raise HTTPException(status_code=400, detail="Invalid input data")
            return json.dumps(get_user(self._client.get_session(), id))

        @self._router.get(self._ENDPOINT_CREATE_USER)
        async def route_createuserGET(name: str, uid: str):
            if not uid or not name:
                raise HTTPException(status_code=400, detail="Invalid input data")
            return json.dumps(create_user(self._client.get_session(), name, uid))

        @self._router.get(self._ENDPOINT_GET_USER)
        async def route_getuserGET(id: str):
            if not id:
                raise HTTPException(status_code=400, detail="Invalid input data")
            return json.dumps(get_user(self._client.get_session(), id))

    @property
    def get_Router(self):
        return self._router