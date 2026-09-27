nome = input("Digite o seu nome: ")
altura = float(input("Digite sua altura em m: "))
peso = float(input("Digite o seu peso em kg: "))
imc = peso / altura ** 2

#o f no print é o f-strings, que serve para colocar variáveis dentro da string
#o :.2f serve para mudar a quantidade de casas decimais, se eu colocar :.20f, vão ter 20 casas decimais
#round serve para arredondar 0 número, deixando com o mínimo de casas decimais possiveis sem alterar significavivamente o valor
print(f"{nome} tem {altura:.2f}m de altura, pesa {peso}kg e seu imc é de: {round(imc,2):.2f}")

