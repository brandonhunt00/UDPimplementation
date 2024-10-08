Implementação UDP em Python - Hello World

Descrição:
Este projeto implementa uma comunicação básica entre cliente e servidor utilizando o protocolo UDP. O servidor escuta mensagens na porta 12345 e, quando um cliente envia uma mensagem, o servidor responde com "Hello World!".

O UDP (User Datagram Protocol) é um protocolo sem conexão que permite o envio de pacotes sem garantia de entrega ou ordem. Essa implementação utiliza a biblioteca socket do Python para criar e gerenciar os datagramas.

Arquivos:
- udp_server.py: Contém a implementação do servidor UDP.
- udp_client.py: Contém a implementação do cliente UDP.

Requisitos:
- Python 3.x
- A biblioteca padrão socket (já incluída no Python)

Como Executar:

Passo 1: Iniciar o servidor
Abra um terminal e execute o seguinte comando para iniciar o servidor:

python udp_server.py

Você verá uma mensagem indicando que o servidor está escutando na porta 12345.

Passo 2: Iniciar o cliente
Em outro terminal, execute o seguinte comando para iniciar o cliente e enviar uma mensagem ao servidor:

python udp_client.py

O cliente enviará uma mensagem para o servidor e receberá a resposta "Hello World!" que será impressa no terminal.

Explicação do Funcionamento:

Servidor (udp_server.py):
1. O servidor cria um socket UDP (socket.AF_INET, socket.SOCK_DGRAM).
2. Ele associa o socket ao endereço localhost na porta 12345.
3. O servidor aguarda receber uma mensagem do cliente usando recvfrom(), que também captura o endereço do cliente.
4. Após receber uma mensagem, o servidor imprime a mensagem e envia de volta "Hello World!" para o endereço do cliente com sendto().
5. O servidor fecha o socket após o envio.

Cliente (udp_client.py):
1. O cliente cria um socket UDP.
2. Ele envia uma mensagem ao servidor em localhost na porta 12345 usando sendto().
3. O cliente aguarda uma resposta do servidor usando recvfrom().
4. A resposta "Hello World!" é impressa no terminal.
5. O cliente fecha o socket após a troca de mensagens.

Observações:
- O protocolo UDP não garante a entrega da mensagem, mas é mais rápido e adequado para aplicações onde a perda de pacotes é aceitável.
- Ao contrário do TCP, o UDP não estabelece uma conexão antes do envio de dados. O cliente simplesmente envia pacotes para o servidor.
