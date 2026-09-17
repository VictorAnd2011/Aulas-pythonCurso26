# Cria comentário
print("Hello, world!") #Printa algo no terminal


"""
cria um DockString
é tipo um comentário multilinha, mas não é um comentário, esse texto 
ele é lido 
"""

#print é uma funcão, e oq vem dentro do () são os argumentos, podendo ter
#mais de 1 argumento, separando eles por vírgula (por padrão já da um espaço automaticamente para separar)
print("tem um número dps",1)

#além disso, também dá quebra de linha automaticamente também
print(12)
print(34)

#Mas é possivel mudar o separador usando sep="", colocando oque quiser como separador
print("sabor", 67,42, sep='-SeparadoR-')

# \r\n quebra de linha de linha no windows -> CRLF
# \n quebra de linha para sistemas unitys -> LF
#com isso, é possivel mudar a quebra de linha, usando o comando end='', que muda oque vem no final do código
#dessa forma, é possivel colocar qualquer coisa no fim, igual o sep
print(67, end='')
print(42, end='-fim do código-')


#o python diferencia letras maiusculas e minusculas, logo, Print() != print()
#logo, caso o comando seja escrito com a letra de forma errada, vai dar erro, como tentar escrevar Print()
#Print("Hello World!") dá erro