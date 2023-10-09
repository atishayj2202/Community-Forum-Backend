from fastapi import FastAPI
from src.routers.userRouter import userRouter
from src.routers.reactionRouter import reactionRouter
from src.routers.postRouter import postRouter
from src.client.cockroach import CockroachDBClient

app = FastAPI()
cli = CockroachDBClient()

app.include_router(userRouter(cli).get_Router)
app.include_router(reactionRouter(cli).get_Router)
app.include_router(postRouter(cli).get_Router)
