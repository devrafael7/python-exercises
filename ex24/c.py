import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 999))

message = input("type something: ")

client_socket.send(message.encode())

data = client_socket.recv(1024).decode()

print(f"message received by the server{data}")

client_socket.close()