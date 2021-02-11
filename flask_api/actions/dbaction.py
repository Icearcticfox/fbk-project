class Action:
    def transaction_insert(self, conn, datadict):
        cur = conn.cursor()
        first_name = datadict["name"]
        last_name = datadict["lastname"]
        corrupt_work = datadict["work"]

        cur.execute(
            """SELECT * FROM public.corruption WHERE first_name = '{first_name}' 
        and last_name = '{last_name}' and corrupt_work = '{corrupt_work}';""".format(
                first_name=first_name, last_name=last_name, corrupt_work=corrupt_work
            )
        )
        result = cur.fetchall()
        if result:
            transaction = {"result": "Такая запись уже существует", "success": False}
        else:
            cur.execute(
                """INSERT INTO public.corruption(id, first_name, last_name, corrupt_work) 
            VALUES (nextval('corruption_sequence_id'), '{first_name}', '{last_name}', '{corrupt_work}');""".format(
                    first_name=first_name,
                    last_name=last_name,
                    corrupt_work=corrupt_work,
                )
            )

            transaction = {"result": "Запись добавлена успешно", "success": True}
            conn.commit()
        return transaction
