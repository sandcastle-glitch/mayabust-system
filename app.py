import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.sqlite')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()

    total_count = conn.execute('SELECT COUNT(*) FROM activations').fetchone()[0]
    total_duration = conn.execute('SELECT SUM(duration) FROM activations').fetchone()[0] or 0
    activations = conn.execute('SELECT * FROM activations ORDER BY timestamp DESC').fetchall()

    conn.close()

    return render_template(
        'overview.html',
        total_count=total_count,
        total_duration=total_duration,
        activations=activations
    )

@app.route('/logs')
def logs():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM activations ORDER BY timestamp DESC').fetchall()
    conn.close()

    return render_template('logs.html', activations=data)

@app.route('/logs/<int:log_id>')
def log_details(log_id):
    conn = get_db_connection()
    log = conn.execute(
        'SELECT * FROM activations WHERE id = ?',
        (log_id,)
    ).fetchone()
    conn.close()

    if log is None:
        return "Log not found", 404

    return render_template('log_details.html', log=log)

if __name__ == '__main__':
    app.run(debug=True, port=5000)