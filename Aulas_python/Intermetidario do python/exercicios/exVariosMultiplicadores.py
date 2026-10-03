def multiplicador(num):
    def multiplicador_x(multi):
        return num * multi

    return multiplicador_x

num = multiplicador(int(input("Digite um número para ser multiplicador: ")))

for multi in range(1,11):
    print(num(multi))

