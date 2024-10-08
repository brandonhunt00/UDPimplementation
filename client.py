import socket

# Criando o socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviando dados para o servidor
client_socket.sendto(b'Hello from client', ('localhost', 12345))

# Recebendo resposta do servidor
data, server = client_socket.recvfrom(1024)
print("Mensagem recebida do servidor:", data.decode())

# Fechando o socket
client_socket.close()
