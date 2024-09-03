import socket

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.bind(('localhost', 80))
servidor_socket.listen(1)

print("aguardando conexão")

cliente_socket, cliente_endereco = servidor_socket.accept()

print(f"conexão estabelecida com{cliente_endereco}")

dados = cliente_socket.recv(1024).decode()

print(f"funcinou, mensagem {dados}")

cliente_socket.send(f'mensagem recebida pelo servidor'.encode())























