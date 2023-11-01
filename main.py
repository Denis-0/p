"""
import pandas as pd
import psycopg2

conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='123',
    host='localhost',
    port='5432'
)

sql_query = "SELECT * FROM employees"
df = pd.read_sql(sql_query, conn)
"""

from sqlalchemy import create_engine
import pandas as pd

# Создаем объект engine для подключения к базе данных
engine = create_engine('postgresql://postgres:123@localhost:5432/postgres')

# Выполняем SQL-запрос с использованием engine
sql_query = "SELECT * FROM public.employees"
df = pd.read_sql_query(sql_query, engine)






"""
cursor = conn.cursor()
insert_query = "INSERT INTO your_table_name (column1, column2) VALUES (%s, %s)"
data = (value1, value2)  # Замените value1 и value2 на фактические значения
cursor.execute(insert_query, data)
conn.commit()


conn.close()
"""


#data = {'Name': ['Alice', 'Bob', 'Charlie'],
#      'Age': [25, 30, 35]}
#df = pd.DataFrame(data)

# print(df.head())  # Первые несколько строк
# print(df.tail())  # Последние несколько строк

# Выбор по названию столбца
# print(df['Name'])

# Выбор по условию
# print(df[df['Age'] > 30])

# Выбор по позиции (по индексу и столбцу)
# print(df.iloc[1, 0])

