from src.client.cockroach import CockroachDBClient
from src.db.reactionHandler import getComments
eng = CockroachDBClient()

print(getComments(eng.get_session(), "1564aa7c-1f87-4c3c-a087-6284f0ae411c"))