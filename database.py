import sqlite3


def create_database():

    conn = sqlite3.connect("passwords.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password_hash TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()
def save_password(username, password_hash):

    conn = sqlite3.connect("passwords.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users(username,password_hash)
        VALUES(?,?)
        """,
        (username, password_hash)
    )

    conn.commit()
    conn.close()    
def password_exists(password_hash):

    conn = sqlite3.connect("passwords.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE password_hash = ?
        """,
        (password_hash,)
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None