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
print(f"F: {f1 / 10000}%")
print(f"C: {c1 / 10000}%\n")


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
print(f"F: {f2 / 10000}%")
print(f"C: {c2 / 10000}% \n")


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
print(f"F: {f3 / 10000}%")
print(f"C: {c3 / 10000}%")