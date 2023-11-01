import psycopg2

# параметры подключения
hostname = 'localhost'  # Адрес сервера базы данныхc
database = 'postgres'   # Имя базы данных
username = 'postgres'   # Имя пользователя
password = '123'        # Пароль

# установка соединения
try:
    connection = psycopg2.connect(
        host=hostname,
        database=database,
        user=username,
        password=password
    )

    # создаем курсор для выполнения SQL-запросов
    cursor = connection.cursor()

    # выполним SQL-запросы с помощью cursor.execute()
    cursor.execute("select * from public.employees")
    result = cursor.fetchall()
    for row in result:
        print(row)
    

    # закрываем курсор и соединение после использования
    cursor.close()
    connection.close()

except Exception as e:
    print("Ошибка подключения:", e)
