import os
opcao = None
lista = []
while opcao != "S":
    opcao = input('\nSelecione uma opção: \n [I]nserir \t [A]pagar \t [L]istar \t [S]air\n').upper()
    os.system("cls")

    if opcao == 'I':
        item_novo = input("Digite o item novo: ")
        lista.append(item_novo)

    elif opcao == 'A':
        item_apagado = input("Digite o índice que deseja apagar: ")
        
        try:
            item_apagado = int(item_apagado)

            try:
                item_apagado = lista.pop(item_apagado)
                print(f"O item {item_apagado} foi apagado!")
            except IndexError:
                print("Não foi possível apagar este índice! tente novamente")

        except ValueError:
            print("Você não digitou um número! tente novamente")

    elif opcao == 'L':
        if lista == []:
            print("Não há itens para listar!")
        else:
            for indice, item in enumerate(lista):
                print(indice, item)  

    elif opcao != 'S':
        print("Você não escolheu nenhuma das opções! Tente novamente!")


print("Saindo...")
        