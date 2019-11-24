import socket
import threading
#import numpy as np
import time


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432       # The port used by the server


def process_data_from_server(x):
    #x1= x.split(",")
    return x


def my_client():
    threading.Timer(11, my_client).start()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    my = input("Enter command ")

    my_inp = my.encode('utf-8')

    s.sendall(my_inp)

    data = s.recv(4096).decode('utf-8')

    cal= process_data_from_server(data)

       
    print(cal)
        

    s.close()
    time.sleep(5)


if __name__ == "__main__":
    while 1:
    	my_client()
