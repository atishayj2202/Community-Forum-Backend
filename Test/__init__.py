from src.client.cockroach import CockroachDBClient
from src.db.postHandler import get_single_Post
eng = CockroachDBClient()

print(get_single_Post(eng.get_session(), "1564aa7c-1f87-4c3c-a087-6284f0ae411c"))