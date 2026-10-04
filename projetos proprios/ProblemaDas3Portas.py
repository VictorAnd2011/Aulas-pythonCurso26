import random
alternativas = ['1F', 'C', '2F']
f1 = 0
c1 = 0
for i in range(1000000):
    random.shuffle(alternativas)
    escolha = random.choice(alternativas)
    if escolha == '1F' or escolha == '2F':
        f1 += 1
    else:
        c1 += 1
print("Mantendo a escolha tivemos:")
print(f"F: {f1 / 10000:.2f}%")
print(f"C: {c1 / 10000:.2f}%\n")


f2 = 0
c2 = 0
for i in range(1000000):
    alternativas = ['1F', 'C', '2F'] #redefine a lita para o padrão


    random.shuffle(alternativas)#embaralhar a lista, para que a escolha seja aleatória


    escolha = random.choice(alternativas)#escolher aleatoriamente um elemento da lista


    #tira um dos errados
    if escolha == '1F':
        alternativas.remove('2F')#remover o outro elemento
    elif escolha == '2F':
        alternativas.remove('1F')#remover o outro elemento
    else:
        alternativas.remove(random.choice(['1F', '2F']))#remover aleatoriamente um dos dois elementos

    escolha = random.choice(alternativas)
    if escolha == '1F' or escolha == '2F':
        f2 += 1
    else:
        c2 += 1

print("Mudando a escolha aleatóriamente tivemos:")
print(f"F: {f2 / 10000:.2f}%")
print(f"C: {c2 / 10000:.2f}% \n")


f3 = 0
c3 = 0
for i in range(1000000):
    alternativas = ['1F', 'C', '2F'] #redefine a lita para o padrão


    random.shuffle(alternativas)#embaralhar a lista, para que a escolha seja aleatória


    escolha = random.choice(alternativas)#escolher aleatoriamente um elemento da lista


    #tira um dos errados
    if escolha == '1F':
        alternativas.remove('2F')#remover o outro elemento
        escolha = 'C'
    elif escolha == '2F':
        alternativas.remove('1F')#remover o outro elemento
        escolha = 'C'
    else:
        alternativas.remove(random.choice(['1F', '2F']))#remover aleatoriamente um dos dois elementos
        if '1F' not in alternativas:
            escolha = '2F'
        else:
            escolha = '1F'
    #muda a escolha


    if escolha == '1F' or escolha == '2F':
        f3 += 1
    else:
        c3 += 1

print("Mudando a escolha para o outro tivemos:")
print(f"F: {f3 / 10000:.2f}%")
print(f"C: {c3 / 10000:.2f}%")
input()
'''
Explicação do problema das 3 portas:
na primeira simulação, o jogador escolhe uma porta e mantém a escolha, então a chance de ganhar é de 1/3
pois são 3 portas e apenas 1 é a correta, então a chance de perder é de 2/3

na segunda simulação, o jogador escolhe uma porta e o apresentador abre uma das portas erradas, 
fazendo com que vc tenha 2 portas para escolher, então a chance de ganhar é de 1/2,
pois são 2 portas e apenas 1 é a correta

já na terceira simulação, vc terá 2/3 de chance de pegar a porta errada na primeira escolha,
e como o apresentador abre uma das portas erradas, quando vc muda a escolha,
vc terá 2/3 de chance de ganhar, pois sempre que você a porta errada, vc mudará para a correta,
pois só restará a porta correta uma errada, então a chance de ganhar é de 2/3

em resumo, a melhor estratégia é sempre mudar a escolha, pois assim vc terá 2/3 de chance de ganhar,
enquanto se vc mantiver a escolha, vc terá apenas 1/3 de chance de ganhar.
e se vc escolher aleatoriamente, vc terá 1/2 de chance de ganhar
'''
