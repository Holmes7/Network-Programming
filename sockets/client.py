import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 55555))
# host and port is specified
message = s.recv(1024)
# receive the message of max size 1024 bytes
s.close()

print(message.decode())
