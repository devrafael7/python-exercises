import tkinter as tk
import server_app
import socket
from datetime import datetime, timedelta
import openpyxl

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.bind(('localhost', 999))
servidor_socket.listen(1)

print("aguardando conexao")

cliente_socket, cliente_endereco = servidor_socket.accept()
time = datetime.now().strftime('%H:%M:%S')

print(f"conexão estabelecida com {cliente_endereco} ás {time}")

dados = cliente_socket.recv(2048).decode()

book = openpyxl.load_workbook('test.xlsx')
info_page = book['info']

if dados == 'Celular':
    server_app.update_dados_app(dados)
    
    server_app.run_server_app()
    
cliente_socket.close()
servidor_socket.close()
    
    


