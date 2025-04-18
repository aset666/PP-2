import csv
import psycopg2

def connect_db():
    return psycopg2.connect(
        host="localhost",
        port="5432",
        dbname="master",
        user="postgres",
        password="qwerty",
        connect_timeout=10,
        sslmode="prefer"
    )

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            phone VARCHAR(15) UNIQUE NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def load_from_csv():
    conn = connect_db()
    cur = conn.cursor()
    with open('phonebook.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Пропускаем заголовок
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s) ON CONFLICT (phone) DO NOTHING",
                row
            )
    conn.commit()
    cur.close()
    conn.close()

def add_from_console():
    conn = connect_db()
    cur = conn.cursor()
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    phone = input("Введите телефон: ")
    cur.execute(
        "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s) ON CONFLICT (phone) DO NOTHING",
        (first_name, last_name, phone)
    )
    conn.commit()
    cur.close()
    conn.close()

def update_data():
    conn = connect_db()
    cur = conn.cursor()
    phone = input("Введите телефон для обновления: ")
    new_first_name = input("Введите новое имя: ")
    cur.execute(
        "UPDATE phonebook SET first_name = %s WHERE phone = %s",
        (new_first_name, phone)
    )
    conn.commit()
    cur.close()
    conn.close()

def query_data():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def delete_data():
    conn = connect_db()
    cur = conn.cursor()
    phone_to_delete = input("Введите телефон для удаления: ")
    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone_to_delete,))
    conn.commit()
    cur.close()
    conn.close()

def main():
    create_table()
    while True:
        print("\n1. Загрузить данные из CSV")
        print("2. Добавить данные через консоль")
        print("3. Обновить данные")
        print("4. Просмотреть все записи")
        print("5. Удалить данные")
        print("6. Выход")
        choice = input("Выберите действие: ")
        
        if choice == '1':
            load_from_csv()
        elif choice == '2':
            add_from_console()
        elif choice == '3':
            update_data()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
