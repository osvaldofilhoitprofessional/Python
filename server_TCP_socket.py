#Socket servidor TCP simples

import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('Iniciando o servidor {} na porta {}'.format(*server_address))
sock.bind(server_address)

sock.listen(1)

while True:
    print("Aguardando uma conexão...\n")
    connection, client_address = sock.accept()
    try:
        print("O cliente {} conectou.".format(client_address))

        while True:
            data = connection.recv(1024)
            print('Recebido: {!r}'.format(data))
            if data:
                print("Enviando os dados para o cliente...\n")
                connection.sendall(data)
            else:
                print("Sem dados do cliente {}.".format(client_address))
                break

    finally:
        connection.close()
