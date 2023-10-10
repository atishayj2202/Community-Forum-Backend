from fastapi import FastAPI
from src.routers.userRouter import userRouter
from src.routers.reactionRouter import reactionRouter
from src.routers.postRouter import postRouter
from src.client.cockroach import CockroachDBClient
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
cli = CockroachDBClient()

# Replace '*' with your Vue.js app's URL in 'allow_origins' to allow requests from your app
origins = ["*"]  # You can specify specific origins if needed

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can specify HTTP methods (e.g., ["GET", "POST"])
    allow_headers=["*"],  # You can specify headers if needed
)


app.include_router(userRouter(cli).get_Router)
app.include_router(reactionRouter(cli).get_Router)
app.include_router(postRouter(cli).get_Router)
