from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pathlib import Path


class CockroachDBClient:
    def __init__(self):
        self.URL = "cockroachdb://atishay:AGEAR3l-dfQmO4i-pbCvUg@air-transfer-12735.5xj.cockroachlabs.cloud:26257/Forum?sslmode=verify-full"
        try:
            self.engine = create_engine(self.URL)
        except Exception as e:
            print("Failed to connect to database.")
            print(f"{e}")

    def get_session(self):
        return sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
