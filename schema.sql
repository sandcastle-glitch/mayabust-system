
CREATE TABLE activations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT (datetime('now','localtime')),
    detection_type TEXT,
    action_taken TEXT,
    duration INTEGER,
    status TEXT DEFAULT 'Success',
    image_path TEXT
);
