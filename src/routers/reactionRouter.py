from fastapi import APIRouter, HTTPException
from src.client.cockroach import CockroachDBClient
import json


class reactionRouter():
    def __init__(self, client: CockroachDBClient):
        from src.db.reactionHandler import addLike, addUnLike, addComment, getComments
        self._ENDPOINT_ADD_LIKE = "/add_like/"
        self._ENDPOINT_ADD_UNLIKE = "/add_unlike/"
        self._ENDPOINT_ADD_COMMENT = "/add_comment/"
        self._ENDPOINT_GET_COMMENTS = "/get_comments/"

        self._client = client
        self._router = APIRouter(prefix="/reaction")

        @self._router.post(self._ENDPOINT_ADD_LIKE)
        async def route_addlikePOST(pid: str):
            if not pid:
                raise HTTPException(status_code=400, detail="Invalid input data")
            return json.dumps(addLike(self._client.get_session(), pid))

        @self._router.get(self._ENDPOINT_ADD_LIKE)
        async def route_addlikeGET(pid: str):
            if not pid:
                raise HTTPException(status_code=400, detail="Invalid input data")
            return json.dumps(addLike(self._client.get_session(), pid))

        @self._router.post(self._ENDPOINT_ADD_UNLIKE)
        async def route_addunlikePOST(pid: str):
            if not pid:
                raise HTTPException(status_code=400, detail="Invalid input data")
            return json.dumps(addUnLike(self._client.get_session(), pid))

        @self._router.get(self._ENDPOINT_ADD_UNLIKE)
        async def route_addunlikeGET(pid: str):
            if not pid:
                raise HTTPException(status_code=400, detail="Invalid input data")
            return json.dumps(addUnLike(self._client.get_session(), pid))

        @self._router.post(self._ENDPOINT_ADD_COMMENT)
        async def route_addcommentPOST(pid: str, body: str, author_id: str):
            if not pid or not body or not author_id:
                raise HTTPException(status_code=400, detail="Invalid input data")
            return json.dumps(addComment(self._client.get_session(), pid, body, author_id))

        @self._router.get(self._ENDPOINT_ADD_COMMENT)
        async def route_addcommentGET(pid: str, body: str, author_id: str):
            if not pid or not body or not author_id:
                raise HTTPException(status_code=400, detail="Invalid input data")
            return json.dumps(addComment(self._client.get_session(), pid, body, author_id))

        @self._router.post(self._ENDPOINT_GET_COMMENTS)
        async def route_getcommentsPOST(pid: str):
            if not pid:
                raise HTTPException(status_code=400, detail="Invalid input data")
            return json.dumps(getComments(self._client.get_session(), pid))

        @self._router.get(self._ENDPOINT_GET_COMMENTS)
        async def route_getcommentsGET(pid: str):
            if not pid:
                raise HTTPException(status_code=400, detail="Invalid input data")
            return json.dumps(getComments(self._client.get_session(), pid))

    @property
    def get_Router(self):
        return self._router
