
import psycopg2


def connect_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="my_database",
            user="postgres",
            password="your_password",
            port="5432"
        )
        cursor = connection.cursor()

        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"Успешное подключение к БД. Версия: {db_version}")

        cursor.close()
        connection.close()
    except Exception as error:
        print(f"Ошибка при работе с PostgreSQL: {error}")


if name == "main":
    connect_db()