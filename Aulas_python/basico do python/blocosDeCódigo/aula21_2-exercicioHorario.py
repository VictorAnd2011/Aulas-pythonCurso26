h = input("Que horas são? ")

try:
    hr = int(h)

    if hr <= 11:
        print("Bom dia!")

    elif hr >= 12 and hr <= 17:
        print("Boa tarde")

    elif hr >=18 and hr <=24:
        print("Boa noite")

    else:
        print("Você não digitou um horário")

except:
    print("Você não digitou um horário")
