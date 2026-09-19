"""
Listas em Python - tipo uma str, mas que dá pra mudar as coisas dentro dela e não é limitado apenas a 
uma letra, mas sim uma coleção de valores.
Tipo list - Mutável
Suporta vários valores de qualquer tipo
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
lista = ['Abóbora', 'Banana', 'Cajá', 'Danone', 'Espinafre']  # 5 elementos (len)
print(lista, type(lista), len(lista))

listaVazia = [] 
print(bool(listaVazia))  # False

#suporta vários tipos de dados
lista2 = [1, 2.5, True, 'Python']
print(lista2)

#dá para acessar os elementos da lista através do índice
print(lista[0])  # Abóbora
print(lista[1])  # Banana
print(lista2[3])  # Python
print(lista2[-1])  # Python

#dá para checar cada item individualmente, como se fosse uma str
print(len(lista[1]))  # 6


#listas são mutáveis, ou seja, dá para mudar os elementos dentro dela
lista[0] = 'Abacaxi'
print(lista[0])


#Caso eu queira apagar um elemento da lista, posso usar o del
del lista[0]
print(lista)  # ['Banana', 'Cajá', 'Danone', 'Espinafre']
#ao apagar um elemento, o índice dos elementos seguintes muda, então o índice 0 agora é 'Banana'


#para adicionar um elemento no final da lista, posso usar o append
lista.append('Figo')
lista.append('Goiaba')
print(lista)  # ['Banana', 'Cajá', 'Danone', 'Espinafre', 'Figo', 'Goiaba']



#para excluir o último elemento da lista, posso usar o pop
lista.pop()
print(lista)  # ['Banana', 'Cajá', 'Danone', 'Espinafre', 'Figo']

#o pop ele retorna o elemento que foi removido, então posso armazenar ele em uma variável
ultimoElemento = lista.pop()
print(ultimoElemento)  # Figo

#o pop também pode receber um índice como parâmetro, e ele vai remover o elemento desse índice
elementoRemovido = lista.pop(1)
print(elementoRemovido)  # Cajá
print(lista)  # ['Banana', 'Danone', 'Espinafre', 'Figo']


#clear() - limpa a lista
lista2.clear()
print(lista2)  # []


#o insert() - insere um elemento em um índice específico
lista.insert(0, 'Acerola') #primeiro parâmetro é o índice, segundo é o elemento
print(lista)  # ['Acerola', 'Banana', 'Danone', 'Espinafre', 'Figo']


#é possivel concatenar listas com o operador +
lista.clear()
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)  # [1, 2, 3, 4, 5, 6]

#é possivel concatenar também com o extend(), continuando a lista original
lista1.extend(lista3)
print(lista1)  # [1, 2, 3, 1, 2, 3, 4, 5, 6]

#listas são iteráveis, então posso usar o for para percorrer cada elemento da lista
for item in lista3:
    print(item)


#o len retorna a quantidade de elementos da lista, dá pra usar isso para ver o indice e o elemento ao mesmo tempo
indices = range(len(lista1))
for indice in indices:
    print(f'Índice: {indice}, Elemento: {lista1[indice]}')


'''
resumindo tudo: 
- Listas são mutáveis
- Suportam vários tipos de dados
- Podem ser concatenadas com + ou extend()
- Elementos podem ser acessados por índice
- Elementos podem ser removidos com del, pop() ou clear()
- Elementos podem ser adicionados com append() ou insert()
'''

lista1.clear()
lista2.clear()
lista3.clear()

#CUIDADOS PARA TOMAR COM LISTAS
#1 - Listas são mutáveis, então se você colocar uma lista apontando para outra,]
# qualquer alteração na primeira vai alterar a segunda também, pois elas estão apontando para o mesmo lugar na memória
lista = ['Maria', 'João', 'Carlos']
lista2 = lista  # lista2 aponta para o mesmo lugar na memória que lista
print(lista2)  # ['Maria', 'João', 'Carlos']]

#Agora, se eu alterar um elemento da lista, a lista2 também vai ser alterada
lista[0] = 'Ana'
print(lista2)  # ['Ana', 'João', 'Carlos']

#Para evitar isso, posso usar o método copy() para criar uma cópia da lista
lista3 = lista.copy()
lista[0] = 'Qualquer coisa'
print(lista)  # ['Qualquer coisa', 'João', 'Carlos']
print(lista3)  # ['Ana', 'João', 'Carlos'] - a lista3 não foi alterada, pois ela é apenas uma cópia da lista original