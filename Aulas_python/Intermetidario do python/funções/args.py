#quando queremos uma quantidade não delimitada de argumentos, podemos usar o *args,
#que é uma tupla de argumentos (pode usar qualquer outro nome, mas a convenção é usar args)

def funcao(*args):
    print(type(args)) #aqui vai imprimir <class 'tuple'>, pois args é uma tupla
    total = 0
    for valor in args:
        total += valor
        print(valor)

    return total

print(funcao(1, 2, 3, 4, 5))

#porém, oque pode acontecer é de eu mandar um argumento que seja uma lista, 
#ai a função vai entender que é apenas um argumento, e não uma quantidade não delimitada de argumentos
# print(funcao([1, 2, 3, 4, 5])) dá erro, pois a função vai entender que é apenas um argumento
#para resolver isso, eu posso usar o * antes da lista,
#ai a função vai entender que é uma quantidade não delimitada de argumentos
numeros = [1, 2, 3, 4, 5, 67, 42, 78]
print(funcao(*numeros)) #aqui vai funcionar, pois a função vai desempacotar a lista