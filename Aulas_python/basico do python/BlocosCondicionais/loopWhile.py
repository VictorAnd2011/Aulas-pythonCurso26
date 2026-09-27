d = "s"
while d.lower().startswith("s"):
    
    d = input("Deseja continuar? [s]im: ")
    if d.lower().startswith("s"):
        print("Você continuou!")

print("Você saiu! ")