#dá pra usar else no while
#Caso o while acabe por uma condição normal, ele executa o else
#Caso o while acabe por conta de um breake, ele não executa

w = True

while w:
    w = input("Quer dar breake? Apenas digite sabor, se não, não digite nada: ")

    if w.lower().startswith("s"):
        print("Não ira aparecer o else")
        break
        

else:
    print("Saiu normalmente, executando o else!")