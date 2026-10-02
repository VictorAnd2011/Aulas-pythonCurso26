'''
funções são determinados trechos de código usados para replicar uma determinada ação
elas podem receber valores para parâmetros (argumentos) e retonar um valor espesífico
por padrão, funções retornam None

o python já vem com várias funções, como o print() por exemplo

é possivel criar uma função
o def cria uma função própria
'''

def sabor(): #cria a função sabor
    print("Tralalelo tralala") #coloca algo para essa função fazer

sabor() #chama a função e replica oq foi escrito para ela fazer
sabor() #ao invés de ter q escrever o mesmo código em lugares diferentes, eu apenas chamo a função


# funções podem recerber valores
def funcao(a, b, c):
    print(a,b,c)

# caso eu não preencha os parametros, vai dar erro
# funcao()
funcao(1,2,3) #está preenchido, então tudo ocorre normalmente
funcao(4,5,6,) # cada vez q eu chamo eu posso passar um valor diferente

# caso eu não queira q de erro ao deixar sem nada preenchido, eu posso deixar um valor pré salvo
def funcao2(nome='Sem nome'):
    print('Olá',nome)

funcao2('Carlos') #funciona como qualquer umsa outra
funcao2() #também funciona, usando o valor pré salvo na função



#Nós temos os argumentos nomeados.
#As vezes, queremos passar os argumentos numa ordem diferente, ou apenas garantir q a varíavel que queremos está 
#recebendo o argumento correto, então, nós apenas colocamos pelo nome do parâmetro

def funcao3(x,y):
    print(f'{x=} {y=}   |   x + y = {x+y}')

funcao3(1,2) #x recebe 1, e y recebe 2
funcao3(2,1) #x recebe 2, e y recebe 1
#mas vamos supor q eu queira manter a ordem mas deixar o 1 no x, e o 2 no y
funcao3(y=2, x=1)
#porém, apartir de quando tu fazer um argumento nomeado, todos os que vierem dps tem q ser nomeados também
# funcao3(y=2, 1) dá errado pois o y que veio antes foi nomeado


#as funções tem escopos, ou seja, variáveis criadas dentro de uma função não podem ser 
#acessadas fora dela

def escopo():
    A = 1
    print(A)

escopo() #aqui funciona, pois a função foi chamada
# print(A) aqui não funciona, pois a variável A foi criada dentro da função

#caso eu crie uma variável fora da função, ela pode ser acessada dentro dela
B = 2  
def escopo2():
    print(B)

escopo2() #aqui funciona, pois a variável B foi criada fora da função, então ela pode ser acessada dentro dela

#Caso eu queria q uma variavavel de dentro da função seja acessada fora dela,
#eu posso usar a palavra global
def escopo_global():
    global C
    C = 3
    print(C)
escopo_global() #aqui funciona, pois a função foi chamada
print(C) #aqui funciona, pois a variável C foi criada dentro da função, mas



#também é possível criar funções dentro de funções, e essas funções internas 
# só podem ser acessadas dentro da função que as criou
def escopo3():
    def escopo_de_dentro():
        print('Função interna')
    escopo_de_dentro() #aqui funciona, pois a função foi chamada dentro da função que a criou

escopo3() #aqui funciona, pois a função foi chamada

#escopo_de_dentro() #aqui não funciona, pois a função foi criada dentro de outra função, e não pode ser acessada fora dela