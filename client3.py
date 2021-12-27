import socket

s = socket.socket()
host = socket.gethostname()
port = 8000
print(socket.gethostname())
s.connect((host, port))
s.send("Client 3")

print (s.recv(1024))
s.close()