from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path='/static')

# Database setup
DATABASE = 'database.db'
STATIC_URL = '/static/'

def create_table():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    #c.execute("DROP TABLE entries")
    c.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            kolegij TEXT NOT NULL,
            nositelj_kolegija TEXT NOT NULL,
            rok1 DATE NOT NULL,
            rok2 DATE NOT NULL,
            rok3 DATE NOT NULL,
            rok4 DATE NOT NULL,
            rok5 DATE NOT NULL,
            rok6 DATE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_table()

@app.route('/')
def index():
    return render_template('stranica.html')

@app.route('/submit', methods=['POST'])
def submit():
    kolegij = request.form['kolegij']
    nositelj_kolegija = request.form['nositelj']
    rok1 = request.form['rok1']
    rok2 = request.form['rok2']
    rok3 = request.form['rok3']
    rok4 = request.form['rok4']
    rok5 = request.form['rok5']
    rok6 = request.form['rok6']

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        INSERT INTO entries (kolegij, nositelj_kolegija, rok1, rok2, rok3, rok4, rok5, rok6)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (kolegij, nositelj_kolegija, rok1, rok2, rok3, rok4, rok5, rok6))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
