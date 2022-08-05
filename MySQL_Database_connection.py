import mysql.connector

# mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="telusko")
mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
mycursor.execute("SELECT * FROM student")
result = mycursor.fetchall()
# print(mycursor)
# for i in mycursor: 	print(i)
for i in result:
    print(i)
