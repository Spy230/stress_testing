import pyodbc
import time

# Подключение к базе данных
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=;'
    'DATABASE=Users;'
   
     'Trusted_Connection=yes;'
)

cursor = conn.cursor()

# Пример простого запроса
start_time = time.time()
cursor.execute("SELECT COUNT(*) FROM Users")
result = cursor.fetchone()
end_time = time.time()
print(f"Время выполнения запроса COUNT: {end_time - start_time} секунд")

# Пример сложного запроса
start_time = time.time()
cursor.execute("SELECT * FROM Users WHERE Email LIKE '%a%'")
result = cursor.fetchall()
end_time = time.time()
print(f"Время выполнения запроса LIKE: {end_time - start_time} секунд")

cursor.close()
conn.close()