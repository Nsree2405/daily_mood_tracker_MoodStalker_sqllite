import mysql.connector

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
def login():
    username = input("Enter username: ")
    email = input("Enter email: ")
    # password = input("Enter password: ")

    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE uname = %s AND email = %s',(username, email))
        user = cursor.fetchone()
        conn.close()
        if user:
            print("Login successful")
            print("User details:")
            print("ID:", user[0])
            print("Username:", user[1])
            print("Email:", user[2])
            print("DOB:",user[3])
        else:
            print("Invalid username, email, or password")
    else:
        print("Database connection error")
 
if __name__ == '__main__':
    login()