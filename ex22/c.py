import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 12345))

message = input("Qual produto você deseja procurar? ")

client_socket.send(message.encode())

data = client_socket.recv(1024).decode()

print(f"Mensagem recebida do servidor: {data}")

client_socket.close()