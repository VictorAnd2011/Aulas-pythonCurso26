num = input("Digite um número inteiro: ")

try:
    num_int = int(num)

    if num_int % 2 == 0:
        print("Seu número é par")
    else:
        print("Seu número é impar")

except:
    print("Seu número não é inteiro")