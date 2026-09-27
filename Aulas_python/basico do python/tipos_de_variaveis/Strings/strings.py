#o python tem um tipo de tipagem dinámica/forte -> isso significa que ele ao ler o código já sabe qual tipo de váriavel vc está usando
#diferente de java, onde vc precisa declarar o tipo antes


#ele já sabe que é uma variável do tipo string, sem a necessidade de declarar ela como str
x = "string"


#str -> string -> texto
#strings são textos dentro de "" ou ''
print('sabor') #ele leu e identificou que era uma string por estar dentro de aspas


#quando eu quero colocar uma aspas dentro da string, a gente usa um caracter de escape, que é o \, isso serve para qualquer outra coisa que vc queira que seja pulada
print("sabor \"67\"")


#caso eu queira que ele mostre o caracter de escape, coloca r antes das aspas
print(r"sabor\"67\"")


#porém, isso deixa o código muito poluido
#então, é muito melhor somente mudar o tipo de aspas
print('oi"tchau"')
print("oi'tchau'")