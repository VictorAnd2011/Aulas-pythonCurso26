# nomes = ['João', 'Maria', 'José']
# nome1, nome2, nome3 = nomes  # desempacotamento de lista
# print(nome1)  # João

# nomes.clear()

# nome1, nome2, nome3 = ('João', 'Maria', 'José')  #funciona de ambas as formas
# print(nome2)  # Maria

#-------

# nome1, nome2 = ['João', 'Maria', 'José']  # desempacotamento de lista com menos variáveis do que elementos dará erro
# nome1, nome2, nome3, nome4 = ['João', 'Maria', 'José']  #também dará erro, pois há mais variáveis do que elementos na lista
#para evitar esse erro, podemos usar o * para desempacotar o restante dos elementos em uma lista
nomes = ['João', 'Maria', 'José', 'Pedro', 'Ana']
nome1, *_ = nomes  # o *_ vai pegar todos os elementos restantes da lista (se usa como convenção o _ para variáveis que não se vai usar)
print(nome1, _)  # João ['Maria', 'José', 'Pedro', 'Ana']

#caso queira pegar o último elemento da lista, podemos fazer assim:
*_, nomeUltimo = nomes  # o *_ vai pegar todos os elementos no começo antes do último elemento
print(nomeUltimo, _)  # Ana

#dá para pegar um do meio também, mas não é muito comum, pois não é tão legível
_, _, nome3, *_ = nomes  
print(nome3)  # José


#Tuplas são listas imutáveis, ou seja, não podem ser alteradas depois de criadas.
#Elas são definidas com parênteses () e podem ser usadas para armazenar múltiplos valores. 
#Ou você pode criar uma tupla apenas não colocando o colchete, como no exemplo abaixo:
tupla = 1, 2, 3, 4, 5
#Tuplas não aceitam métodos de adição ou remoção de elementos, mas aceitam métodos de contagem e indexação.
#O desempacotamento de tuplas funciona da mesma forma que o desempacotamento de listas.