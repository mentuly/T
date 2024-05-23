import sqlite3


def create_schedule_database():
    conn = sqlite3.connect('school_schedule.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Schedule (
                    id INTEGER PRIMARY KEY,
                    day TEXT,
                    lesson_number INTEGER,
                    subject TEXT
                )''')
    
    schedule_data = [
        ("Понеділок", 1, "Хімія"),
        ("Понеділок", 2, "Алгебра"),
        ("Понеділок", 3, "Українська мова"),
        ("Понеділок", 4, "Англійська мова"),
        ("Понеділок", 5, "Біологія"),
        ("Вівторок", 1, "Англійська мова"),
        ("Вівторок", 2, "Фізичне виховання"),
        ("Вівторок", 3, "Українська мова"),
        ("Вівторок", 4, "Фізика"),
        ("Вівторок", 5, "Алгебра"),
        ("Середа", 1, "Історія України"),
        ("Середа", 2, "Географія"),
        ("Середа", 3, "Алгебра"),
        ("Середа", 4, "Геометрія"),
        ("Середа", 5, "Англійська мова"),
        ("Четвер", 1, "Англійська мова"),
        ("Четвер", 2, "Українська мова"),
        ("Четвер", 3, "Інформатика"),
        ("Четвер", 4, "Українська література"),
        ("Четвер", 5, "Хімія"),
        ("П'ятниця", 1, "Фізика"),
        ("П'ятниця", 2, "Всесвітня історія"),
        ("П'ятниця", 3, "Зарубіжна література"),
        ("П'ятниця", 4, "Алгебра"),
        ("П'ятниця", 5, "Геометрія"),
    ]
    for data in schedule_data:
        cur.execute("INSERT INTO Schedule (day, lesson_number, subject) VALUES (?, ?, ?)", data)
    conn.commit()
    conn.close()

def display_schedule():
    conn = sqlite3.connect('school_schedule.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Schedule")
    schedule = cur.fetchall()
    print("Розклад уроків:")
    for lesson in schedule:
        print(f"{lesson[1]} - {lesson[2]} урок: {lesson[3]}")
    conn.close()

create_schedule_database()
display_schedule()