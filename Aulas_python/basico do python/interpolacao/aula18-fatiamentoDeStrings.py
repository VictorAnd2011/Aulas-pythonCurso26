'''
 012345678
 ola mundo   
-987654321

fatiamento [i:f:p] [::]
i = inicio
f = fim
p = passo (de quantos em quantos caracteres ele vai pular)
'''

var = "Olá mundo"
print(var[4:]) #vai fatiar e pegar apenas do indice 4 para frente (se eu omito o fim, ele vai até o ultimo)
print(var[4:7])
print(var[4:8]) #se eu quiser que o indice 7 apareça, eu coloco 8, pois é onde ele vai parar de contar
print(var[:5]) #se eu omito o inicio, ele vai a partir do primeiro

#len retorna a qtd de caracteres na str
print(len(var)) #mostra quantos caracteres tem na variavel
print(len(var[4:7])) #mostra quantos caracteres tem na fatia que nós escolhemos

#o p é de quantos em quantos caracteres ele vai ler, o padrão é de 1 em 1
print(var[::1])#vai de 1 em 1, lendo todos
print(var[::2])#vai de 2 em 2, lendo apenas alguns
print(var[::3])#vai de 3 em 3

#se eu colocar um número negativo, ele vai começar a ler os indices negativos, que são invertidos
print(var[::-1])#vai de 1 em 1, mas ao contrário
print(var[::-2])#vai de 2 em 2 ao contrário

