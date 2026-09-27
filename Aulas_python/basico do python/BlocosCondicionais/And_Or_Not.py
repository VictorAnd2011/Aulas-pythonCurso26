#and serve para quando se precisa de ambas as condições verdadeira
x = int(input("x deve ser 1 para verdadeiro: "))
y = int(input("y deve ser 2 para verdadeiro: "))
if x == 1 and y ==2: #só vai ser true se ambos forem verdadeiros
    print("Ambos certos")
else:
    print("Pelo menos 1 falso")

#or serve pra quando se precisa apenas de 1 verdadeira pelo menos
if x == 1 or y == 2:
    print("Pelo menos 1 certo")
else:
    print("Ambos falsos")

#not é pra quando se precisa que a condição seja falsa para que ela passe
if not x == 1:
    print("X é falso, mas o if verdadeiro")
else:
    print("X é verdadeiro, mas o if falso")

#caso eu queira que algo seja avaliado primeiro, se usa parenteses
us = input("Digite o user: ")
senha_user = input("Digite a senha: ")
senha_certa = '6742'
if (us == "E" or us == "e") and senha_user == senha_certa: #colocou entre parenteses para garantir que não haja ambiguidades
    print("Acesso liberado")
else:
    print("Acesso negado")