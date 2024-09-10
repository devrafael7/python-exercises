import socket
import openpyxl
import servidor_app

servidor_app.servidor_app_run()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor_socket:
    servidor_socket.bind(('localhost', 80))
    servidor_socket.listen(1)
    
    print("Servidor escutando..")

    cliente_socket, cliente_endereco = servidor_socket.accept()

    dados = cliente_socket.recv(1024).decode()

    planilha_produtos = openpyxl.load_workbook('Estoque (1).xlsx').active
    primeira_linha = [cell.value for cell in planilha_produtos[1]]
    
    linhas_encontradas = []

    for cada_linha in planilha_produtos.iter_rows(min_row=2, values_only=True):
        linha_encontrada = False 
        for cell in cada_linha:
            if dados in str(cell):
                linha_encontrada = True
                break  
        if linha_encontrada:
            linhas_encontradas.append(cada_linha)
    
    quantidade_total = 0
    
    for coluna_quantidade in linhas_encontradas:
        quantidade_total += coluna_quantidade[4]

    linhas_texto = ''
    
    if linhas_encontradas:
        for linha in linhas_encontradas:
            linhas_texto += str(linha) + '\n'

    servidor_app.adicionar_valores_app(
        f"{primeira_linha}\n\n{linhas_texto}\n\nTotal de Quantidade de Estoque: {quantidade_total}"
    )

    cliente_socket.send('Os dados foram entregues'.encode())
    servidor_app.root.mainloop()



















