import socket

sock = socket.socket()
print ("Socket created ...")

port = 50000
sock.bind(('', port))
sock.listen(1)

print ('socket is listening')

while True:
    c, addr = sock.accept()
    print ('got connection from ', addr)
    
    jsonReceived = c.recv(1024)
    
    print ("Json received -->", jsonReceived)
   
    #c.close()
