import mysql.connector
from mysql.connector import Error

# Database connection parameters
host = 'localhost'
database = 'oracle'
user = 'root'
password = 'aim@1432'

try:
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT distinct users.uname , users.gender,  moods.mname, moods.activity, feels.day from users,moods,feels where feels.uid=users.uid and feels.mid=moods.mid;")
        data = cursor.fetchall()

        html_content = """
        <!doctype html>
        <html lang="en">
          <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <!-- Bootstrap CSS -->
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">

            <title>Data Table</title>
          </head>
          <body>
            <div class="container mt-5">
              <h2>Data Table</h2>
              <table class="table table-striped">
                <thead>
                  <tr>
                    <th>a</th>
                    <th>b</th>
                    <th>c</th>
                    <th>d</th>
                    <th>e</th>
                  </tr>
                </thead>
                <tbody>
        """

        # Populate the table rows with data
        for row in data:
            html_content += f"""
                  <tr>
                    <td>{row[0]}</td>
                    <td>{row[1]}</td>
                    <td>{row[2]}</td>
                    <td>{row[3]}</td>
                    <td>{row[4]}</td>
                  </tr>
            """

        # Close the HTML content
        html_content += """
                </tbody>
              </table>
            </div>

            <!-- Optional JavaScript; choose one of the two! -->

            <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/js/bootstrap.bundle.min.js"></script>

          </body>
        </html>
        """

        # Write the HTML content to a file
        with open("data_table.html", "w") as file:
            file.write(html_content)

        print("HTML file has been generated successfully.")

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")