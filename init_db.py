import sqlite3
import os

folder = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(folder, 'database.sqlite')

def create_fresh_db():

    if os.path.exists(db_path):
        os.remove(db_path)
        print("Deleted old database.")

    conn = sqlite3.connect(db_path)

    conn.execute('''
        CREATE TABLE activations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT (datetime('now','localtime')),
            detection_type TEXT,
            action_taken TEXT,
            duration INTEGER,
            image_path TEXT
        )
    ''')

    conn.commit()
    conn.close()

    print(f"Success! Fresh database created at: {db_path}")

if __name__ == "__main__":
    create_fresh_db()