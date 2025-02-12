from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Function to create a connection to the MySQL database
def create_connection():
    conn = None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='aim@1432',
            database='oracle'
        )
    except mysql.connector.Error as e:
        print(e)
    return conn

# Function to login and retrieve user details
def login(username, email):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE uname = %s AND email = %s', (username, email))
        user = cursor.fetchone()
        conn.close()
        return user
    else:
        return None

# Route to render the login form
@app.route('/')
def index():
    return render_template('login.html')

# Route to handle login form submission
@app.route('/login', methods=['POST'])
def login_submit():
    username = request.form['username']
    email = request.form['email']

    user = login(username, email)
    if user:
        return jsonify({'message': 'Login successful', 'user': {'id': user[0], 'username': user[1], 'email': user[2]}})
    else:
        return jsonify({'message': 'Invalid username, email, or password'}), 401

if __name__ == '__main__':
    app.run(debug=True)