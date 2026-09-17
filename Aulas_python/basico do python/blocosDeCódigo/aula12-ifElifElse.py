#if  /elif     /else
#se /se não se/ se não

en = input("Você quer 'entrar' ou 'sair'? ")


#as condicionais servem para pular certas partes do código dependendo da condição
#se o if for executado, ele vai ignorar o else
#e se o else for executado, vai ignorar o if]

#se a condição for verdadeira, vai executar oq está dentro do bloco if
if en == "entrar":
    print("Você entrou")

#se ela for falsa, vai executar oque está dentro do bloco else
else:
    if en == "sair":
        print("Você saiu")
    else:
        print("erro, você não digitou nem entrar, nem sair")

#em blocos de código, para ver oque está dentro doq, se usa o espaçamento para a borda da tela (indentação)
#se algo estiver com mais identação que o código anterior, ele vai estar dentro dele


#nós temos também o elif, que encurta a sequencia de else: if:
pre = input('vc prefere "67" ou "42"? ')

if pre == "67":
    print("vc é resenha")

elif pre == "42": #diminui para um código só, ao inves de else e dps if
    print("vc é beta")

else:
    print("vc não me respondeu felas")