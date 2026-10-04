print('====== BANCO ======')
input('Presione enter para começar... ')
print()

database = []

opcoes_login = ('Criar conta','Entrar na conta')

opcoes = ('Consultar saldo','Depositar','Sacar','Transferir','Sair')

def validando_nome(nome):
    if not nome.replace(' ', '').isalpha():
        return False
    return True


def validando_senha(senha):
    if senha.isalpha():
        return False
    elif senha.isdigit():
        return False
    elif senha.islower():
        return False
    elif len(senha) < 8:
        return False

    else:
        return True


def validando_cpf(cpf):
    digitos = []
        
    for digito in cpf:
        if digito.isdigit():    
            digitos.append(digito)

    if len(digitos) != 11:
        return False

    elif len(set(digitos)) == 1:
        return False

    def validador(digitos_calculados):
        soma = 0
        for n in range(digitos_calculados):
            soma += int(digitos[n]) * ((digitos_calculados+1)-n)

        resto11 = (soma * 10) % 11
        digito = resto11 if resto11 <=9 else 0

        if int(digitos[digitos_calculados]) == digito:
            return True
        else:
            return False

    digito1 = validador(9)
    digito2 = validador(10)

    if not(digito1 or digito2):
        return False
    return True
            

def criar_conta():
    user = {
    'saldo':0
}
    print('\n--- CRIE SUA CONTA ---\n')
    tudo_certo = False

    while tudo_certo==False:
        nome_digitado=input('Digite o seu nome: ')
        nome_valido = validando_nome(nome_digitado)

        cpf_digitado = input('Digite seu CPF: ')
        cpf_valido = validando_cpf(cpf_digitado)
        


        senha_digitada = input('Escolha uma senha: ')
        senha_valida = validando_senha(senha_digitada)


        if nome_valido:
            user.setdefault('nome_salvo', nome_digitado)
        else:
            print('\nNOME inválido!!!')

        if senha_valida:
            user.setdefault('senha_salva',senha_digitada)
        else:
            print('\nSENHA inválida!!!')

        if cpf_valido:
            user.setdefault('cpf_salvo',cpf_digitado)
        else:
            print('\nCPF inválido!!!')


        if nome_valido and senha_valida and cpf_valido:
            tudo_certo = True
            print('\n---CONTA CRIADA COM SUCESSO---\n')
            database.append(user)
        else: 
            print('\n---Tente novamente---\n').upper()


def pedindo_opcoes(opcoes):
    for indice, opcao in enumerate(opcoes):
        print(f'{indice+1}) {opcao}')
    escolha = input('Qual das opções deseja realizar? ')
    return escolha-1

pedindo_opcoes(opcoes_login)






