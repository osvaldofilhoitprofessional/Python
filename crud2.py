
cpfs = {'9090': 'Osvaldo', '9898': 'Toim'}

while True:
    print('Digite um CPF: (em branco para encerrar)')
    cpf = str(input())

    if cpf == '':
        break

    if cpf in cpfs:
        print('O CPF do usuário ' + cpfs[cpf] + ' existe!')
    else:
        print('Não há informação sobre o ' + cpf)
        print('Qual o nome do usuário?')
        nome = str(input())
        cpfs[cpf] = nome
        print('Banco de CPF\'s atualizado!')
