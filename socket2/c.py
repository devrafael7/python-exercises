import tkinter as tk  
import cliente_app
import socket 
from datetime import datetime, timedelta
import openpyxl

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(('localhost', 999))

cliente_app.run_app()
cliente_socket.send(cliente_app.mensagem.encode())

dados = cliente_socket.recv(2048).decode()