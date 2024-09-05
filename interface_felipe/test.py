import tkinter as tk
##(Criação da janela principal)

root = tk.Tk()
root.title("GDP")

root.geometry("500x500")
root.config(bg="white")

##(Título)

titulo_label = tk.Label(root, text="Qual eletrônico você quer? ")
titulo_label.pack(pady=10)

##(Entrada do texto)

entrada = tk.Entry(root, width=30)
entrada.pack(pady=10)

##(Configuração do botão)

def clicar_botao():
    nome = entrada.get()
    print(f"Nome digitado: {nome}")

botao = tk.Button(root, text="Enviar", command=clicar_botao)
botao.pack(pady=10)

root.mainloop()