from src.client.db import CockroachDBClient
from src.db.main import get_All_Post

eng = CockroachDBClient()

print(get_All_Post(eng.get_session()))