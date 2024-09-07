import socket
import cliente_app

cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente_socket.connect (('localhost',80))

cliente_app.clienteApp_run()
mensagem = cliente_app.nome
cliente_socket.send(mensagem.encode())

dados = cliente_socket.recv(1024).decode()

cliente_socket.close()