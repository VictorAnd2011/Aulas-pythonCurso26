def multiplicar(*args):
    multiplicador = 1
    for num in args:
        num = float(num)
        multiplicador *= num

    return multiplicador

nums = input("Digite os números que quer multiplicar: ").split()

print(multiplicar(*nums))