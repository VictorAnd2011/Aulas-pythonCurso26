perguntas = [
    {
        "pergunta": "Qual é a capital da França?",
        "alternativas": ["Londres", "Berlim", "Madrid", "Paris"],
        "resposta": "Paris"
    },
    {
        "pergunta": "Quanto é 2 + 2?",
        "alternativas": ["3", "4", "5", "6"],
        "resposta": "4"
    },
    {
        "pergunta": "Qual é o maior planeta do sistema solar?",
        "alternativas": ["Terra", "Júpiter", "Saturno", "Marte"],
        "resposta": "Júpiter"
    },
    {
        'pergunta': 'Qual é a fórmula da área de um circulo?',
        'alternativas': ['πr²', '2πr²', '2hπr','Cosθπr²'],
        'resposta': 'πr²'
    },
]
acertos = 0
erros = 0
print('---JOGO DE PERGUNTAS E RESPOSTAS---')

for questao in perguntas: #pega questão por questão
    print(f'\n{questao['pergunta']}') #mostra a pergunta

    for indice, alt in enumerate(questao['alternativas']): #para cada alternativa, mostra ela e o indice
        print(f'{indice}) {alt}')

    try:
        escolha = int(input("Escolha uma alternativa: ")) #pega a escolha do jogador

        if questao['resposta'] == questao['alternativas'][escolha]: #vê se a resposta é igual a alternativa escolhida
            print('\nAcertou!')
            acertos += 1
        else:
            print('\nErrou!')
            erros += 1

    except (ValueError, IndexError):
        print('\nVOCÊ NÃO DIGITOU UMA ALTERNATIVA!!!')
        erros +=1



print(f'\nVOCÊ ACERTOU {acertos} QUESTÕES!')
print(f'E ERROU {erros} QUESTÕES!')
input()
