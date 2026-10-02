#quando queremos que uma função retorne algum valor para dentro de uma variavel
#usamos a palavra return

def soma(x,y):
    print(x+y) #aqui a função soma não retorna nada, apenas printa o resultado da soma

soma1 = soma(1,2) #aqui a função retorna None, apenas printa o resultado da soma
print(soma1) #aqui vai imprimir None

def soma(x,y):
    return x+y #aqui a função soma retorna o resultado da soma

soma2 = soma(1,2) #aqui a função retorna o resultado da soma
print(soma2) #aqui vai imprimir 3
#isso é util quando queremos que a função retorne algum valor para ser usado em outra parte do código, 
#ou para ser armazenado em uma variável

soma1 = soma(1,2) 
soma2 = soma(3,4) 
print(soma1 + soma2) #aqui vai imprimir 10, pois soma1 é 3 e soma2 é 7



#tudo que vem depois do return não é executado, 
#pois a função já retornou o valor e saiu dela
def soma(x,y):
    print('OLHA')
    print('QUE')
    print('LEGAL')
    print('TÁ')
    print('SENDO')
    print('EXECUTADO!')
    return x+y
    print('isso não vai ser executado')

print(soma(1,2))