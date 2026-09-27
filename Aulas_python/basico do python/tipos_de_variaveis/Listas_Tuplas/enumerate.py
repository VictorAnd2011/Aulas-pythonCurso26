#enumerate serve para conseguir ver o indice do item e o item junto, ele retorna uma tupla com o índice e o item
lista = ['João', 'Maria', 'José']
lista_enumerada = enumerate(lista)
print(next(lista_enumerada))  # (0, 'João')

#para ver todos os elementos enumerados, podemos usar um for
for item in lista_enumerada:
    print(item)  # (1, 'Maria') (2, 'José')

#um problema do enumerate é que ele não reinicia o índice, então se você quiser reiniciar o índice, 
# você pode usar a função enumerate novamente

for item in lista_enumerada:
    print(item)  # não vai imprimir nada, pois o enumerate já foi consumido

for item in enumerate(lista): #assim vai funcionar, pois estamos criando um novo enumerate
    print(item)  # (0, 'João') (1, 'Maria') (2, 'José')



#também tem a opção de transformar o enumerate em uma lista, assim podemos ver todos os elementos enumerados de uma vez
lista_enumerada = list(enumerate(lista))
print(lista_enumerada)  # [(0, 'João'), (1, 'Maria'), (2, 'José')]


#muitas vezes, queremos apenas o índice ou apenas o item,
#  então podemos usar o desempacotamento de tuplas para pegar apenas o que queremos
for item in enumerate(lista):
    indice, nome = item  # desempacotamento da tupla
    print(indice, nome)  # 0 João 1 Maria 2 José

#mas tem uma forma mais simples de fazer isso, que é usando o desempacotamento direto no for
for indice, nome in enumerate(lista):
    print(indice, nome)  # 0 João 1 Maria 2 José