import sqlite3


DB_NAME = 'shell.db'

# Connection to the SQLite database
def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                command TEXT UNIQUE NOT NULL,
                description TEXT,
                payload TEXT NOT NULL
                )
    """)
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                command_name TEXT,
                executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT
                )
    """)

    conn.commit()
    conn.close()