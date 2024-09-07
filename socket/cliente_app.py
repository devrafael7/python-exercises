import tkinter as tk

nome = None

def clienteApp_run():
    global nome

    def enviar():
        global nome
        nome = input_field.get()
        root.destroy()  

    root = tk.Tk()
    root.title("Controle de Estoque - Cliente")
    root.geometry("300x200")

    label = tk.Label(root, text="Digite o nome do produto:", bg="white")
    label.pack(pady=20)

    input_field = tk.Entry(root, width=20, font=('Arial', 16))
    input_field.pack(pady=10)

    btn = tk.Button(root, text="Enviar", command=enviar)
    btn.pack(pady=10)

    root.mainloop()