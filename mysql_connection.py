import mysql.connector

MYDB = mysql.connector.connect(
    host="localhost",
    user="myusername",
    passwd="mypassword"
)

print(MYDB)
