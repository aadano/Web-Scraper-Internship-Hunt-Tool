from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("events.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM events ORDER BY date")
    events = cursor.fetchall()
    conn.close()
    return render_template('index.html', events=events)

if __name__ == '__main__':
    app.run(debug=True)