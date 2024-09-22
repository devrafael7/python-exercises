import socket  # Importa o socket, que permite a comunicação via redes

# Cria um socket para o cliente com o protocolo IPv4 (AF_INET) e o protocolo TCP (SOCK_STREAM)
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta o cliente ao servidor que está rodando no 'localhost' e na porta 80
cliente_socket.connect(('localhost', 80))

# Solicita ao usuário para digitar a marca ou modelo procurado
mensagem = input("Procure pela marca ou modelo do automóvel: ")

# Envia a mensagem digitada pelo usuário para o servidor, codificando para bytes antes de enviar
cliente_socket.send(mensagem.encode())

# Recebe a resposta do servidor de até 1024 bytes, decodifica de bytes para string e armazena na variavel 'dados'
dados = cliente_socket.recv(1024).decode()

# Exibe a mensagem recebida do servidor
print(dados)

# Fecha a conexão do cliente com o servidor.
cliente_socket.close()
