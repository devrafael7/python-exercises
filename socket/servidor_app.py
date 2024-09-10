import tkinter as tk

def servidor_app_run():
    global apl_texto, root
    root = tk.Tk()
    root.title("Controle de Estoque - Servidor")

    apl_texto = tk.Text(font=("Helvetica", 12))
    apl_texto.pack(fill="both", expand=True)

def adicionar_valores_app(todos_valores):
    apl_texto.insert("end", f"{todos_valores}\n")
    root.update_idletasks()