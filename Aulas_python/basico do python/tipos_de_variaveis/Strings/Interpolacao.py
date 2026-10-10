# s - string
# f - float
# d e i - int
# x e X - hexadecimal

nome = input("Digite seu nome: ")
preco = 67.42678194
variavel = "%s, o preço é R$%.2f" % (nome, preco)
print(variavel)

#hexadecimal serve para converter um número normal para hexadecimal
ex = int(input("Digite um número: "))
print("o hexadecimal de %d é %x" % (ex, ex))