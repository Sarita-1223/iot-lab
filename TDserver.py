import socket      
import time 
  
# initializing socket 
s = socket.socket()      
host = '127.0.0.1'  
port = 12345
  
# binding port and host 
s.bind((host, port))    
  
# waiting for a client to connect 
s.listen(5)   
         
while True: 
   # accept connection 
   c, addr = s.accept()         
   print ('got connecton from addr', addr) 
   date = time.asctime() 
   d = str(date) 
  
   # sending data type should be string and encode before sending 
   c.send(d.encode())       
   c.close() 
