import socket
import threading
import time
import sqlite3

HOST = '127.0.0.2'  
PORT = 65432       


def process_data_from_server(x):
    x1= x.split(",")
    return x1


def my_client():
    threading.Timer(11, my_client).start()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        my = input("Enter command ")

        my_inp = my.encode('utf-8')

        s.sendall(my_inp)

        data = s.recv(1024).decode('utf-8')

        ipaddress= process_data_from_server(data)

       
        print(ipaddress)

      #Open database connection
conn = sqlite3.connect("TESTDB" )

# prepare a cursor object using cursor() method
cursor = conn.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS addr")

# Create table as per requirement

conn.execute("CREATE TABLE addr (IP  CHAR(90))");
print("\\connected To Db")

# Prepare SQL query to INSERT a record into the database.
sql= "INSERT INTO addrd(IP)VALUES(?)"

try:
   # Execute the SQL command
    cursor.execute(sql,[ipaddress])
   # Commit your changes in the database
    conn.commit()
except:
   # Rollback in case there is any error
       conn.rollback()  
       conn.close()

time.sleep(5)


if __name__ == "__main__":
    while 1:
        my_client()
