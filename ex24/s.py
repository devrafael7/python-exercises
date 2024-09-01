import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 999))
server.listen(5)

print('waiting for connection')

client_socket, client_addres = server.accept()

print(f"connection established with{client_addres}")

data = client_socket.recv(1024).decode()

print('it worked out')

client_socket.send('message received by the server'.encode())