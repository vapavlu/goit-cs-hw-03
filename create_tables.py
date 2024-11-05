import psycopg2

# Параметри підключення
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Створення таблиці users
cursor.execute('''
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
''')

# Створення таблиці status
cursor.execute('''
CREATE TABLE status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);
''')

# Створення таблиці tasks
cursor.execute('''
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER REFERENCES status(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);
''')

# Додати статуси в таблицю status
cursor.execute("INSERT INTO status (name) VALUES ('new'), ('in progress'), ('completed');")

conn.commit()
cursor.close()
conn.close()
