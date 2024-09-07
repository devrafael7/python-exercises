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
    primeira_linha = [str(cell.value) for cell in planilha_produtos[1]]
    
    linhas_encontradas = [
        row for row in planilha_produtos.iter_rows(min_row=2, values_only=True) 
        if any(dados.lower() in str(cell).lower() for cell in row)
    ]
    
    quantidade_total = sum(row[4] for row in linhas_encontradas)
    linhas_texto = "\n".join(map(str, linhas_encontradas)) if linhas_encontradas else "Não encontrado."

    servidor_app.adicionar_primeira_linha(
        f"{primeira_linha}\n\n{linhas_texto}\n\nTotal de Quantidade de Estoque: {quantidade_total}"
    )

    cliente_socket.send('Os dados foram entregues'.encode())
    
    servidor_app.root.mainloop()



















