import psycopg2

# параметры подключения
hostname = 'localhost'  # Адрес сервера базы данных
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
    cursor.execute("""INSERT INTO public.employees_1(employee_id, first_name, last_name, salary)
                        SELECT employee_id, first_name, last_name, salary
                        FROM public.employees""")
    #result = cursor.fetchall()
    #for row in result:
    #    print(row)
    # Завершаем транзакцию и сохраняем изменения
    connection.commit()

    # закрываем курсор и соединение после использования
    cursor.close()
    connection.close()

except Exception as e:
    print("Ошибка подключения:", e)
