import sqlite3

def init_db():
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT,
            date TEXT,
            deadline TEXT,
            location TEXT,
            link TEXT UNIQUE,
            description TEXT,
            source TEXT
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized!")