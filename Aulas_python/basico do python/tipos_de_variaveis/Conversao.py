#A conversão de tipos (convertion) é mudar um tipo de variável para outro
#Como por exemplo mudar algo de int para str

#para mudar algum tipo de dado para outro, basta botar o nome do tipo de dado com () e o dado dentro
#ex: int(), flaot(), str(), bool()

x = "1"
#se eu não mudar o tipo de str para int, vai dar erro
#print(x + 1) dá erro
print(int(x) + 1)
print(type(int(x)))

print(type(float(x)))
print(float(x) + 1) #por ser um flaot, mesmo que não tenha casa decimal, ela vai aparecer
print(float(x))

#só a possivel transformar numéros em float ou int
#print(float("teste"))
#print(int("teste"))



#para conversão para bool, quando está vazio ele dá False, e quando tem algo dentro dá True
print(bool('')) #dá false pois não tem nada dentro
print(bool(' ')) #dá true pois tem algo dentro
print(bool(0)) #dá false quando é 0, e true para qualquer outro valor
print(bool(1))

#é possivel converter para str também, para permitir a concatenação
print(str(1) + "b")
print(type(str(1)))

#resumo:
print(int("1"))#para converter para int
print(float("1"))#para converter para float
print(str(1))#para converter para str
print(bool(1))#para converter para bool
