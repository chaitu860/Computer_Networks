import socket

s = socket.socket()
host = socket.gethostname()
port = 5001

s.connect((host, port))
s.send("Client 1")

s.recv(1024)
s.close()
