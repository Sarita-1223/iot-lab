
import socket
import encodings




HOST = '127.0.0.2' 
PORT = 65432      




def hostaddress():
    hostname = socket.gethostname() 
    IP = socket.gethostbyname(hostname) 
    return IP
    

def my_server():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print("Server Started waiting for client to connect ")
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()

    with conn:
        print('Connected by', addr)
        while True:

            data = conn.recv(1024).decode('utf-8')

            if str(data) == "Data":

                print("Ok Sending data ")

                my_data = hostaddress()

                x_encoded_data = my_data.encode('utf-8')

                conn.sendall(x_encoded_data)
                print(my_data)

            elif  str(data) == "Quit":
                print("shutting down server ")
                break

                
            else:
                pass

IP=hostaddress()
#sql = ''' create table Ipaddress(IP_addr text) '''
#sql = ''' insert into Ipaddress values(IP)'''
#sql= ''' select * from Ipaddress '''
#cur.execute(sql)
#val=cur.fetchone()[0]
print(IP)
#conn.commit()
#cur.close()


if __name__ == '__main__':
    while (1):
        my_server()
