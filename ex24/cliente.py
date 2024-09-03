import socket

cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente_socket.connect (('localhost',80))
mensagem = input("escreva algo: ")
cliente_socket.send (mensagem.encode())

dados = cliente_socket.recv(1024).decode()