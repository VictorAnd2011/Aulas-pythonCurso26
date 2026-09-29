continuar = 's'
while continuar == 's':
    cpf = input("Digite seu CPF: ")
    digitos = []
    

    for digito in cpf:
        if digito.isdigit():    
            digitos.append(digito)

    if len(digitos) != 11:
            print("Você não digitou o CPF corretamente!")
            continue        
    elif len(set(digitos)) == 1:
         print("CPF inválido! Não são permitidos número repitidos!")

    else:
        soma = 0
        for n in range(9):
            soma += int(digitos[n]) * (10-n)



        multiplicacao = soma * 10
        resto11 = multiplicacao % 11
        digito1 = resto11 if resto11 <=9 else 0

        print("Primeiro digito válido!" if int(digitos[9]) == digito1 else "Primeiro digito inválido!")

        soma_2 = 0
        for n in range(10):
            soma_2 += int(digitos[n]) * (11-n)

        multiplicacao_2 = soma_2 * 10
        resto11_2 = multiplicacao_2 % 11
        digito2 = resto11_2 if resto11_2 <=9 else 0

        print("Segundo digito válido!" if int(digitos[10]) == digito2 else "Segundo digito inválido!")


    continuar = input("Deseja continuar(S ou N): ").lower()

