def par_impar(numero):
    if numero % 2 == 0:
        return f"{numero} é Par"
    return f"{numero} é Impár"

num = int(input("Digite um número inteiro: "))
print(par_impar(num))