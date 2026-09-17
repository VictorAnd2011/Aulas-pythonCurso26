nome = input('qual o seu nome felas?\n')
print(f'seu nome é {nome} felas')

#o input sempre recebe dados como string
#logo, tentar fazer contas com esses dados dará erro
# erro = input('digite um numero felas\n')
# i = erro + 2
# print(i)


#para isso não acontecer, é possivel colocar int(input())
n = int(input("fala um número"))
i = n ** 2
print(i)
#porém, isso não é recomendado, pois caso o usuário digite uma letra, isso vai quebrar o código
#por isso, é melhor criar um segunda variável para converter o número, assim podendo antes verificar se realmente aquilo é um número antes de converter
m = input("fala outro número")
mInt = int(m)
print(mInt)