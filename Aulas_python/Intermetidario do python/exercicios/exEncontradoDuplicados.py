def Duplicados(lista):
    lista_set = set()

    menor_repetido = -1
    #para cada item do set, ele verificara se repete, quando repetir pela primeira vez, ele volta e verifica o próximo número
    #guardando o menor indice de número repetido
    for indice, item in enumerate(lista):
        lista_temp = lista_set.copy()
        lista_set.add(item)
        if lista_set == lista_temp:
            menor_repetido = indice
            break

    return menor_repetido




lista = list(input('Digite uma lista com itens duplicados separados por espaço: ').split(' '))
indice_duplicado = Duplicados(lista)

if indice_duplicado != -1:
    print(f'O primeiro item que foi achado duplicado foi: {lista[indice_duplicado]}, no índice {indice_duplicado}')
else:
    print('Não teve nenhum duplicado!')

