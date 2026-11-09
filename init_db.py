import sqlite3

connection = sqlite3.connect('sto.db')
cursor = connection.cursor()

# Видаляємо старі таблиці, якщо вони існують, щоб уникнути дублювання
cursor.execute('DROP TABLE IF EXISTS services')
cursor.execute('DROP TABLE IF EXISTS orders')

# Створюємо таблицю послуг
cursor.execute('''
    CREATE TABLE services (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER NOT NULL
    )
''')

# Створюємо таблицю заявок (клієнтів)
cursor.execute('''
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_name TEXT NOT NULL,
        phone TEXT NOT NULL,
        service_id INTEGER,
        FOREIGN KEY (service_id) REFERENCES services (id)
    )
''')

# Наповнюємо прайс-лист послугами
cursor.execute("INSERT INTO services (name, price) VALUES ('Заміна масла', 500)")
cursor.execute("INSERT INTO services (name, price) VALUES ('Комп''ютерна діагностика', 350)")
cursor.execute("INSERT INTO services (name, price) VALUES ('Заміна гальмівних колодок', 800)")
cursor.execute("INSERT INTO services (name, price) VALUES ('Ремонт ходової', 1500)")
cursor.execute("INSERT INTO services (name, price) VALUES ('Шиномонтаж (4 колеса)', 600)")

# Наповнюємо базу даних тестовими клієнтами (заявками)
cursor.execute("INSERT INTO orders (client_name, phone, service_id) VALUES ('Олександр Іваненко', '+38 (050) 123-45-67', 1)")
cursor.execute("INSERT INTO orders (client_name, phone, service_id) VALUES ('Марія Коваленко', '+38 (067) 987-65-43', 2)")
cursor.execute("INSERT INTO orders (client_name, phone, service_id) VALUES ('Василь Петренко', '+38 (063) 111-22-33', 3)")
cursor.execute("INSERT INTO orders (client_name, phone, service_id) VALUES ('Олена Сидоренко', '+38 (099) 444-55-66', 1)")

connection.commit()
connection.close()

print("Базу даних 'sto.db' успішно створено та наповнено послугами і клієнтами.")