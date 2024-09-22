import socket  # Importa o socket, que permite a comunicação via redes
import openpyxl  # Importa o openpyxl, que permite a leitura e manipulação de arquivos Excel

# Cria um objeto socket para o servidor, que usará o protocolo IPv4 (AF_INET) e o protocolo TCP (SOCK_STREAM)
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define o endereço IP e a porta ('localhost' e porta 80)
servidor_socket.bind(('localhost', 80))

# Coloca o servidor em modo de escuta, aceitando apenas a 1 conexão
servidor_socket.listen(1)
print("Aguardando conexão...")

# Aceita a conexão do cliente e retorna um novo socket para a comunicação com o cliente.
cliente_socket, cliente_endereco = servidor_socket.accept()
print(f"Conexão estabelecida com {cliente_endereco}")

# Recebe dados do cliente de até 1024 bytes e decodifica de bytes para string.
dados = cliente_socket.recv(1024).decode()
print(f"Funcionou, mensagem: {dados}")

# Envia uma resposta de volta ao cliente
cliente_socket.send('Mensagem recebida pelo servidor'.encode())

# Abre o arquivo Excel 'Estoque (1) (1).xlsx' usando a biblioteca 'openpyxl'.
arquivo_excel = openpyxl.load_workbook('Estoque (1) (1).xlsx')

# Define a aba ativa no excel
pagina = arquivo_excel.active

# Coleta e armazena os valores da primeira linha do arquivo Excel 
primeira_linha = [celula.value for celula in pagina[1]]
print('\nCabeçalhos:', primeira_linha)

# Criação da lista de produtos
produtos = []

# Itera sobre todas as linhas da planilha, começando da linha 2, e pega os valores apenas (values_only=True)
for cada_linha in pagina.iter_rows(min_row=2, values_only=True):
    
    # Variavel pra identificar se o produto foi encontrado(Falso ou Verdadeiro)
    produto_encontrado = False
    
    for celula in cada_linha:
        
        # Verifica se o dado recebido do cliente está em alguma célula da linha
        if dados.lower() in str(celula).lower():
            
            # Se o dado for encontrado,a variavel identificadora passa a ser verdadeira
            produto_encontrado = True
            break
    
    # Se o produto for encontrado, adiciona a linha completa à lista 'produtos'
    if produto_encontrado:
        produtos.append(cada_linha)

# Exibe a lista de produtos encontrados
print('\nProdutos encontrados:')
for produto in produtos:
    print(produto)

# Calcula o estoque total
estoque_total = sum(produto[4] for produto in produtos)
print('\nTotal de produtos referente à pesquisa:', estoque_total)

# Fecha a conexão com o cliente.
cliente_socket.close()

# Fecha o socket do servidor
servidor_socket.close()
