import sqlite3

def init_db():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    # Create a table for doctors/users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    # Add a demo user (only if they don't exist)
    try:
        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", 
                       ('doctor@healthcenter.com', 'admin123'))
        conn.commit()
    except sqlite3.IntegrityError:
        pass 
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized!")


    import sqlite3

def update_db():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    # Create history table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doctor_email TEXT,
            patient_name TEXT,
            symptoms TEXT,
            prediction TEXT,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (doctor_email) REFERENCES users (email)
        )
    ''')
    conn.commit()
    conn.close()

update_db()
