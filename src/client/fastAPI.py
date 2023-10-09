from fastapi import FastAPI
from src.routers.userRouter import userRouter
from src.client.cockroach import CockroachDBClient

app = FastAPI()
cli = CockroachDBClient()

app.include_router(userRouter(cli).get_Router)
