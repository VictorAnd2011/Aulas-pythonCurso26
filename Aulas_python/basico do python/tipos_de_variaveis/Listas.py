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
