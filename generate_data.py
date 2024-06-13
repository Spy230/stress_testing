import pyodbc
import random
import string

# Функция для генерации случайных данных
def generate_data(size):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))

# Подключение к базе данных
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=;'
    'DATABASE=Users;'
    
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()


# Генерация и вставка данных
for _ in range(100000):  # Генерация 100,000 записей
    first_name = generate_data(10)
    last_name = generate_data(10)
    email = generate_data(15) + "@example.com"
    cursor.execute("INSERT INTO Users (FirstName, LastName, Email) VALUES (?, ?, ?)", 
                   first_name, last_name, email)

conn.commit()
cursor.close()
conn.close()