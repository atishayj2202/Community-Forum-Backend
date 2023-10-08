from src.client.db import CockroachDBClient
from src.db.articleHandler import add_Post
eng = CockroachDBClient()

print(add_Post(eng.get_session(), "Hello Tony Lets make Some power", "I'm Asshole", "Apple", "79f4bba1-c7b4-4d4a-a011-2a6b66f2b332"))