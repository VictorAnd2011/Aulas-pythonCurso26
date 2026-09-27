'''
o for cria um laço de repetição,
que é utilizado para percorrer uma sequência (como uma lista, tupla, dicionário, conjunto ou string)
e executar um bloco de código para cada item da sequência.

ele é usando quando já se sabe o número de iterações que serão feitas,
ou seja, quando se sabe quantas vezes o bloco de código será executado.
'''

for i in range(5): #range(5) cria uma sequência de números de 0 a 4
    print(i) #printa o valor de i a cada iteração

#for funciona com strings, listas, tuplas, dicionários e conjuntos
for letra in "Python": #percorre cada letra da string
    print(letra) #printa a letra a cada iteração

for numero in [1, 2, 3, 4, 5]: #percorre cada número da lista
    print(numero) #printa o número a cada iteração
