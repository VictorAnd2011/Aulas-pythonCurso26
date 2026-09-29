import random

digitos = []
for n in range(9):
    digitos += str(random.randint(0,9))

soma = 0
for n in range(9):
    soma += int(digitos[n]) * (10-n)

multiplicacao = soma * 10
resto11 = multiplicacao % 11
digito1 = resto11 if resto11 <=9 else 0

digitos.append(str(digito1))

soma_2 = 0
for n in range(10):
    soma_2 += int(digitos[n]) * (11-n)

multiplicacao_2 = soma_2 * 10
resto11_2 = multiplicacao_2 % 11
digito2 = resto11_2 if resto11_2 <=9 else 0

digitos.append(str(digito2))


cpf = ''.join(digitos)
print("O CPF gerado foi: ", cpf)
