n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

if n1 < n2:
    print(f"{n2=} é maior que {n1=}")
elif n2 < n1:
    print(f"{n2=} é menor que {n1=}")
else:
    print(f"{n2=} é igual á {n1=}")