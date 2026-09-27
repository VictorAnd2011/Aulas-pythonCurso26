palavra = "PARAlelePIPEdo".lower()
acertos = '-' * len(palavra)
ganhou = True
erros = 0

print('---JOGO DA FORCA---')
input('Aperte enter para começar...')

while acertos != palavra:
    l_chute = input("\nDigite uma letra: ").lower()

    if l_chute == palavra:
        print('Você acertou o chute!!!')
        break


    if len(l_chute) > 1:
        print("CHUTE ERRADO!!!")
        erros += 1
        continue


    if l_chute in palavra:
        print(f'{l_chute} estava na palavra!')


        i = 0
        for i in range(len(palavra)):
            l = palavra[i]
            if l == l_chute:
                acertos = acertos[:i] + l_chute + acertos[i+1:]
        print(acertos)


    else:
        print(f'{l_chute} NÃO estava na palavra...')
        print(acertos)
        erros += 1


print(f'\nVocê acertou a palavra {palavra.upper()}! Errando apenas {erros} vezes!!!')