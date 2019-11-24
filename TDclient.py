import sqlite3
import socket 
s = socket.socket() 
host = '127.0.0.1' 
port = 12345
  
# connect to host 
s.connect((host, port)) 
  
# recv message and decode here 1024 is buffer size.
a=s.recv(1024).decode()
print (a)    


#Open database connection
conn = sqlite3.connect("TESTDB" )

# prepare a cursor object using cursor() method
cursor = conn.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS TIME1")

# Create table as per requirement

conn.execute("CREATE TABLE TIME1 (d1  CHAR(90))");
print("\\connected To Db")

# Prepare SQL query to INSERT a record into the database.
sql= "INSERT INTO TIME1(d1)VALUES(?)"

try:
   # Execute the SQL command
   cursor.execute(sql,[a])
   # Commit your changes in the database
   conn.commit()
except:
   # Rollback in case there is any error
   conn.rollback()

# disconnect from server
conn.close()

# disconnect from server

s.close() 


