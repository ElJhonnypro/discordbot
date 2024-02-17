from flask import Flask, render_template, send_from_directory
import sqlite3

app = Flask(__name__)

DATABASE = '../database/secretos.db'

@app.route('/css/<filename>')
def cssreturn(filename):
    return send_from_directory('css',filename)

def connect_db():
    return sqlite3.connect(DATABASE)

@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM secrets')
    database = cursor.fetchall()
    conn.close()
    return render_template('home.html', database=database)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)