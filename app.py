from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Define database path dynamically
DB_PATH = os.path.join(os.path.dirname(__file__), 'instance', 'moodtracker.db')

# Function to create a connection to the SQLite database
def create_connection():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row  # Enables dictionary-like access
        return conn
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return None

# Function to retrieve user details
def get_user_details(username, email, password):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE uname = ? AND email = ? AND passkey = ?', (username, email, password))
        user_details = cursor.fetchone()
        conn.close()
        return user_details
    return None

# Function to retrieve user mood details
def get_user_mood_details(username):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT users.uname, feels.day, feels.scale, feels.cause, moods.mname, moods.type, moods.booster, moods.activity
            FROM users
            JOIN feels ON users.uid = feels.uid
            JOIN moods ON feels.mid = moods.mid
            WHERE users.uname = ?
        ''', (username,))
        user_mood_details = cursor.fetchall()
        conn.close()
        return user_mood_details
    return None

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/get_user_details', methods=['POST'])
def get_user_details_submit():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    user_details = get_user_details(username, email, password)
    user_mood_details = get_user_mood_details(username)

    if user_details and user_mood_details:
        return render_template('user_details.html', user_details=user_details, user_mood_details=user_mood_details)
    else:
        return render_template('user_not_found.html')

@app.route('/record_mood_page', methods=['GET'])
def record_mood_page():
    return render_template('record_mood.html')

@app.route('/record_mood', methods=['POST'])
def record_mood():
    date = request.form['date']
    mood = request.form['mood']
    scale = request.form['scale']
    cause = request.form['cause']
    username = request.form['username']

    conn = create_connection()
    if conn:
        cursor = conn.cursor()

        # Get user ID
        cursor.execute('SELECT uid FROM users WHERE uname = ?', (username,))
        user = cursor.fetchone()
        if user is None:
            return 'User not found.'

        user_id = user[0]

        # Get mood ID
        cursor.execute('SELECT mid FROM moods WHERE mname = ?', (mood,))
        mood_data = cursor.fetchone()
        if mood_data is None:
            return 'Mood not found.'

        mood_id = mood_data[0]

        # Insert mood record
        cursor.execute('INSERT INTO feels (uid, mid, day, scale, cause) VALUES (?, ?, ?, ?, ?)',
                       (user_id, mood_id, date, scale, cause))
        conn.commit()
        conn.close()
        return 'Mood recorded successfully!'
    return 'Failed to connect to the database.'

if __name__ == '__main__':
    app.run(debug=True, port=5001)
