#é possivel colocar listas dentro de listas

salas = [
['Maria', 'João', 'Carlos'],
['Marcos','Cleiton'],
['Jonas', 'Celide', (0, 10, 20, 30, 40)]
]

print(salas)
print(salas[2])#Vai acessar a lista 2
print(salas[2][2])#Vai acessar o indice 2 da lista 2
print(salas[2][2][2])#Vai acessar o indice 2 da tupla 2 na lista 2

#para deixar mais bonito, dá para desempacotar dentro de um print
print(*salas, sep='\n')
