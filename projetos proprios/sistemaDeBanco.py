import os
print('====== BANCO ======')
input('Presione enter para começar... ')
print()

database = [{'saldo':67.50,'cpf_salvo':'50043685897','senha_salva':'Victor123@'}]

opcoes_registro = ('Criar conta','Entrar na conta')

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
    'saldo':0.0
}
    print('\n--- CRIE SUA CONTA ---\n')
    tudo_certo = False

    while tudo_certo==False:
        nome_digitado=input('Digite o seu nome: ')
        nome_valido = validando_nome(nome_digitado)

        cpf_digitado = input('Digite seu CPF: ')
        cpf_valido = validando_cpf(cpf_digitado)
        for indice, _ in enumerate(database):
            if cpf_digitado == database[indice]['cpf_salvo']:
                cpf_valido = False
            
       

        senha_digitada = input('Escolha uma senha: ')
        senha_valida = validando_senha(senha_digitada)


        if nome_valido:
            user['nome_salvo'] = nome_digitado
        else:
            print('\nNOME inválido!!!')

        if senha_valida:
            user['senha_salva'] = senha_digitada
        else:
            print('\nSENHA inválida!!!')

        if cpf_valido:
            user['cpf_salvo'] = cpf_digitado
        else:
            print('\nCPF inválido!!!')


        if nome_valido and senha_valida and cpf_valido:
            tudo_certo = True
            os.system('cls')
            print('\n---CONTA CRIADA COM SUCESSO---\n')
            database.append(user)
            logado = True
            indice_do_user = database.index(user)
            return logado, indice_do_user
        else:
            os.system('cls')
            print('\n---TENTE NOVAMENTE---\n')


def login():
    while True:
        cpf_d = input('\nDigite o CPF da conta: ')

        senha = input('Digite a senha: ')
    
        for indice, _ in enumerate(database):
            if cpf_d == database[indice]['cpf_salvo']:
                if senha == database[indice]['senha_salva']:
                    logado = True
                    indice_do_user = indice
                    os.system('cls')
                    print('\n---LOGIN EFETUADO COM SUCESSO---\n')
                    return logado, indice_do_user
        os.system('cls')        
        print('\n---CPF ou SENHA inválidos---\n')

            
def consultar_saldo():
    os.system('cls')
    saldo = f'\nSeu saldo é de: {database[indice_user]['saldo']}R$\n'
    return saldo

def depositar():
    os.system('cls')
    deposito = float(input('Quanto deseja depositar: '))
    database[indice_user]['saldo'] = database[indice_user]['saldo'] + deposito
    deposito = f'\nForam depositados {deposito:.2f}R$, totalizando {database[indice_user]['saldo']:.2f}R$\n'
    return deposito


def pedindo_opcoes(opcoes):
    global opcoes_registro_funcao, opcoes_funcao
    opcoes_registro_funcao = (criar_conta,login)
    opcoes_funcao = (consultar_saldo,depositar,)
    for indice, opcao in enumerate(opcoes):
        print(f'{indice+1}) {opcao}')
    escolha = int(input('Qual das opções deseja realizar? '))
    return escolha-1



logado = False
while logado == False:
    escolha_registro = pedindo_opcoes(opcoes_registro)
    user_logado = opcoes_registro_funcao[escolha_registro]()
    logado, indice_user = user_logado

while True:
    escolha = pedindo_opcoes(opcoes)
    print(opcoes_funcao[escolha]())











