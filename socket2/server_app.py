import tkinter as tk
import socket

dados_app = None
def run_server_app():
    root = tk.Tk()
    root.geometry("500x600")
    root.title("server_app")
    root.config(bg="white")

    global dados_app
    dados_app = tk.Label(root, text="Qual item deseja procurar?", bg="white")
    dados_app.place(relx=0.490, rely=0.1, anchor="center")

    root.mainloop()
    
def update_dados_app(message):
    global dados_app
    if dados_app:
        dados_app.config(text=message)
        
    
    