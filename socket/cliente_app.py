import tkinter as tk
##(Criação da janela principal)

nome = ''

def clienteApp_run():
    global nome
    
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
        global nome
        nome = entrada.get()

    botao = tk.Button(root, text="Enviar", command=clicar_botao)
    botao.pack(pady=10)

    root.mainloop()