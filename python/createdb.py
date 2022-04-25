import psycopg2


class Db:
    def __init__(self, database, user, password, host, port):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def _connect(self):
        conn = psycopg2.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        conn.autocommit = True

        cursor = conn.cursor()

        return conn, cursor

    def create_db(self):
        conn, cursor = self._connect()


        sql = "CREATE DATABASE database"

        cursor.execute(sql)
        print("Database created successfully")

        conn.close()

    def create_table(self, table_name):
        conn, cursor = self._connect()

        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

        number_columns = int(input('Введите число столбцов: '))

        table_rows = ''

        for i in range(0, number_columns):
            table_rows += (str(input('Введит строку для создания поля(без запятой): ')))
            if i < number_columns - 1:
                table_rows += ','
                table_rows += '\n'
        print(table_rows)

        sql = f"""
        CREATE TABLE {table_name}
        (
        {table_rows}
        )
        """

        print(sql)
        #
        # sql1 = f"""
        # CREATE TABLE {table_name}
        # (
        # table_date DATE NOT NULL,
        # name TEXT  NOT NULL,
        # amount INT NOT NULL,
        # distance INT NOT NULL
        # )
        # """
        #
        cursor.execute(sql)
        print("table created successfully")
        conn.commit()
        conn.close()

    def insert_data(self, table_name, number_columns, amount_rows):
        for i in range(0, amount_rows):
            # number_columns = int(input('Введите число столбцов: '))
            conn, cursor = self._connect()

            values_table = ""

            for i in range(number_columns):
                values = input(f"Введите значение для строки {i + 1}: ")
                values_table += "\'" + values + "\'"

                if i < number_columns - 1:
                    values_table += ','
                    values_table += '\n'

            print(values_table)

            cursor.execute(f"""
            INSERT INTO {table_name} VALUES (
            {values_table}
            )
            """)

            conn.commit()
            print("Records inserted")

            conn.close()


db = Db('postgres', 'postgres', 'password', 'localhost', '5432')
# db.create_db()
# db.create_table('database_table')
db.insert_data('database_table', 4, 3)


