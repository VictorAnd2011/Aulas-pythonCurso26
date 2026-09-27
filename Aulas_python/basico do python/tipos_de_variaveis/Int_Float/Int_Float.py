#int são numero inteiros
x = 1
y = -1
z = 0
print(x,y,z)

#flaot são numeros com ponto flutuante (numeros não inteiros, com virgula, fração, etc)
x2 = 1.1
y2 = 0.67
z2 = -1.1
print(x2,y2,z2)

#na programação, se usa o . para casas decimais, e não a virgula
#logo 1,1 daria seria lido como outra coisa
x3 = 1,1
print(x3)

#caso eu queira ver qual o tipo da variavel que eu estou usando, posso usar a função type()
print(type(x)) #falará que é int
print(type(x2)) #falará que é float
print(type(x3), end="\n\n") #falará que é outra coisa (usei \n\n para separar do próximo)
#isso funciona para str tambem e para coisas direto nele

print(type("sabor"))
print(type(1))
print(type(1.1))

