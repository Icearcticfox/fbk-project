import psycopg2
import json


class Action:
    def __init__(self):
        try:
            self.conn = psycopg2.connect("dbname='postgres' user='admin' host='db' password='secret'")
            #self.conn = psycopg2.connect("dbname='postgres' user='admin' host='localhost' password='secret'")
        except:
            print("I am unable to connect to the database")

        self.cur = self.conn.cursor()

    def transaction_insert(self, datadict) -> json:
        first_name = datadict["name"]
        last_name = datadict["lastname"]
        corrupt_work = datadict["work"]

        self.cur.execute("""SELECT * FROM public.corruption WHERE first_name = '{first_name}' 
        and last_name = '{last_name}' and corrupt_work = '{corrupt_work}';""".
                         format(first_name=first_name,
                                last_name=last_name,
                                corrupt_work=corrupt_work))
        result = self.cur.fetchall()
        print(result)
        if result:
            transaction = {"result": "Такая запись уже существует", "success": False}
        else:
            self.cur.execute("""INSERT INTO public.corruption(id, first_name, last_name, corrupt_work) 
            VALUES (nextval('corruption_sequence_id'), '{first_name}', '{last_name}', '{corrupt_work}');""".
                             format(first_name=first_name,
                                    last_name=last_name,
                                    corrupt_work=corrupt_work))

            transaction = {"result": "Запись добавлена успешно", "success": True}
            self.conn.commit()
        self.conn.close()
        return transaction
