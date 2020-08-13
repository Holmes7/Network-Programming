import socket

# Internet socket
# Communication between processs over the network

# Unix Socket
# data exchange between processes over the same machine

# Protocols
# 1. TCP
#	 Better for accurate data transfer. Example for
#	 sending messages. Hence we use it here.
# 2. UDP
# 	 Better for fast data transfer. Video Games Skype etc

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 55555))
s.listen()

while True:
	client, address = s.accept()
	print(f'Connected to {address}')
	client.send('You are connected'.encode())
	client.close()
