import psycopg2
from faker import Faker

fake = Faker()

# Параметри підключення
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Додати випадкових користувачів
for _ in range(10):
    fullname = fake.name()
    email = fake.email()
    cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

# Додати випадкові завдання
for _ in range(20):
    title = fake.sentence()
    description = fake.text()
    status_id = fake.random_int(min=1, max=3)  # Статуси 1, 2, 3
    user_id = fake.random_int(min=1, max=10)   # Користувачі 1 до 10
    cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", 
                   (title, description, status_id, user_id))

conn.commit()
cursor.close()
conn.close()
