import tkinter as tk

def servidor_app_run():
    global apl_texto, root

    root = tk.Tk()
    root.title("Controle de Estoque - Servidor")

    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    apl_texto = tk.Text(frame, wrap="word", yscrollcommand=scrollbar.set, font=("Helvetica", 12))
    apl_texto.pack(fill="both", expand=True)

    scrollbar.config(command=apl_texto.yview)

def adicionar_primeira_linha(primeira_linha):
    apl_texto.insert("end", f"{primeira_linha}\n")
    root.update_idletasks()