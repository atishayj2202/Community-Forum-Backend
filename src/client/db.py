from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class CockroachDBClient:
    def __init__(self):
        data_dir
        self.URL  = "cockroachdb://atishay:uWM3SX4cuvWlW5I5uaM5ig@air-transfer-12735.5xj.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert=/Users/atishayjain/PycharmProjects/Project-AirTransfer-Server-Backend/cert/db.crt"
        try:
            self.engine = create_engine(self.URL)
        except Exception as e:
            print("Failed to connect to database.")
            print(f"{e}")
    def get_session(self):
        print("HERE")
        return sessionmaker(autocommit=False, autoflush=False, bind=self.engine)