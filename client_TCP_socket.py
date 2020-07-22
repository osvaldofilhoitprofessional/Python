#Socket cliente simples TCP

import socket

server_ip = socket.gethostbyname("localhost")
print("\nO endereço do servidor solicitado é {}.".format(server_ip))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print("Conectando ao servidor {} na porta {}.".format(*server_address))
sock.connect(server_address)

try:
    message = input("Digite sua mensagem para o servidor: \n")
    print('Enviando... {!r}'.format(message))
    data = bytes(message, encoding='utf8')
    sock.sendall(data)

    dados_recebidos = 0
    dados_esperados = len(message)

    while dados_recebidos < dados_esperados:
        data = sock.recv(1024)
        dados_recebidos += len(data)
        print('Recebido: {!r}'.format(data))

finally:
    print("Encerrando a conexão...")
    sock.close()
