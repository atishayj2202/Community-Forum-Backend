from src.client.cockroach import CockroachDBClient
from src.db.userHandler import get_user
eng = CockroachDBClient()

print(get_user(eng.get_session(), "d66d24fb-d32c-49db-b69a-ff08beade403"))