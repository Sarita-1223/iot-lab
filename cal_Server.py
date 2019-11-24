import calendar
#import numpy as np
import socket
import encodings
import sqlite3

HOST = '127.0.0.1'
PORT = 65432

def getcal():
    yy = 2019
    #mm = 10
    cal = calendar.calendar(yy) 
    print(cal)
    return cal
    hadd = socket.gethostbyname(socket.gethostname())
    print(hadd)
    return hadd

    import sqlite3

db = sqlite3.connect("MyDB")
cur = db.cursor()
cur.execute("Drop table If EXISTS ADDR1")
cur.execute("Create table ADDR1(AddrHost char(20))")
cur.execute("Insert into ADDR1(AddrHost) values('hadd')")

db.close()


def my_server():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Server started waiting for client to connect")
	s.bind((HOST,PORT))
	s.listen(5)
	conn, addr = s.accept()

	with conn:
		while True:
			data = conn.recv(4096).decode('utf-8')
			if str(data) == "Data":
				print("OK Sending data")
				my_data = getcal()
				encoded_data = my_data.encode('utf-8')
				conn.sendall(encoded_data)
			elif str(data) == "Quit":
				print("Shut down server")
				break
			else:
				pass

if __name__ == '__main__':
	while (1):
		my_server()
		getcal()


