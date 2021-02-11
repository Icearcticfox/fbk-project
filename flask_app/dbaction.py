import json
import os

import psycopg2
from logaction import logger


class Action:
    def __init__(self):
        host = os.getenv("HOST")
        user = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWORD")
        dbname = os.getenv("POSTGRES_DB")
        try:
            self.conn = psycopg2.connect(
                "dbname={dbname} user={user} host={host} password={password}".format(
                    host=host, user=user, password=password, dbname=dbname
                )
            )
        except:
            logger.error("Unable to connect to the database")

        self.cur = self.conn.cursor()

    def transaction_insert(self, datadict) -> json:
        first_name = datadict["name"]
        last_name = datadict["lastname"]
        corrupt_work = datadict["work"]

        self.cur.execute(
            """SELECT * FROM public.corruption WHERE first_name = '{first_name}' 
        and last_name = '{last_name}' and corrupt_work = '{corrupt_work}';""".format(
                first_name=first_name, last_name=last_name, corrupt_work=corrupt_work
            )
        )
        result = self.cur.fetchall()
        print(result)
        if result:
            transaction = {"result": "Такая запись уже существует", "success": False}
        else:
            self.cur.execute(
                """INSERT INTO public.corruption(id, first_name, last_name, corrupt_work) 
            VALUES (nextval('corruption_sequence_id'), '{first_name}', '{last_name}', '{corrupt_work}');""".format(
                    first_name=first_name,
                    last_name=last_name,
                    corrupt_work=corrupt_work,
                )
            )

            transaction = {"result": "Запись добавлена успешно", "success": True}
            self.conn.commit()
        self.conn.close()
        return transaction
