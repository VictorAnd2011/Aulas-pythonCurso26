import random

print("---JOGO DE ADIVICAÇÃO---")
input("Pressione enter para começar...")

chute = 0
tentativas = 0
numero = random.randint(1,100)
while chute != numero:
    chute = int(input("\nChute um número: "))

    if chute == numero:
        print(f'VOCÊ ACERTOU EM APENAS {tentativas} TENTATIVAS!!!')

    elif chute > numero:
        print('O número é menor!')
        tentativas += 1

    else:
        print('O número é maior!')
        tentativas += 1

input()
