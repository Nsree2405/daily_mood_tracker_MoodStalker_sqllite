import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="aim@1432",
  database="oracle"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM feels")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

