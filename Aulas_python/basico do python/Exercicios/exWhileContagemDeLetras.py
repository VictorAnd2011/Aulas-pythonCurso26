frase = ""

while (frase == "") or (frase.isspace()):
    frase = input("Digite o seu texto: ")
    if (frase == "") or (frase.isspace()):
        print("Você não digitou nada! TENTE NOVAMENTE!")
    

i = 0
qtd_max = 0
qtd_empate = None
l_max = None

while i < len(frase):

    l_atual = frase[i]
    qtd_atual = frase.count(l_atual)

    if (qtd_atual == qtd_max) and (l_atual != l_max):
        l_empate = l_atual
        qtd_empate = qtd_atual

    if (qtd_atual > qtd_max) and not " " == l_atual:
        l_max = l_atual
        qtd_max = qtd_atual

    i += 1



if qtd_max == qtd_empate:
    print(f'A letra {l_empate.upper()} e a letra {l_max.upper()} empataram, com as duas aparecendo {qtd_max} vezes!')
else:
    print(f'A letra que mais apareceu foi {l_max.upper()}, aparecendo {qtd_max} vezes!')
    
    