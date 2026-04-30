import sqlite3
import os

folder = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(folder, 'database.sqlite')

def create_fresh_db():
    if os.path.exists(db_path):
        os.remove(db_path)
        print("Deleted old database.")

    conn = sqlite3.connect(db_path)
    
    # Updated Table with more 'Thesis-Grade' columns
    conn.execute('''
        CREATE TABLE activations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT (datetime('now','localtime')),
            detection_type TEXT,
            action_taken TEXT,
            duration INTEGER
        )
    ''')
    
    # Add dummy rows to see the difference in the logs
    sample_data = [
        ('PIR Sensor', 'Buzzer + LED', 15),
        ('Ultrasonic', 'LED Flash', 5),
        ('Manual Test', 'System Check', 2)
    ]
    
    conn.executemany(
        "INSERT INTO activations (detection_type, action_taken, duration) VALUES (?, ?, ?)", 
        sample_data
    )
    
    conn.commit()
    conn.close()
    print(f"Success! Database updated with new columns at: {db_path}")

if __name__ == "__main__":
    create_fresh_db()