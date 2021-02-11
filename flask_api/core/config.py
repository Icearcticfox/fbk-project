import os

import psycopg2


class Config:
    def get_db(self):
        host = os.getenv("HOST")
        user = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWORD")
        dbname = os.getenv("POSTGRES_DB")
        conn = psycopg2.connect(
            "dbname={dbname} user={user} host={host} password={password}".format(
                host=host, user=user, password=password, dbname=dbname
            )
        )
        return conn
