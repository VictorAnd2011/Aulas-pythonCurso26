#strings são iteráveis (se pode navegar por cada letra da string)
# 0  1  2  3  4  5
# V  i  c  t  o  r
#-6 -5 -4 -3 -2 -1
nome = "Victor"
print(nome[2]) #procura pela letra que está no índice 2 (c)
print(nome[-4]) #funciona também com o índice negativo

#é possivel verificar se algo está dentro da variavel com o in
print("V" in nome) #Retorna true, pois tem V na variável nome
print("M" in nome) #Retorna false, pois não tem M na variável nome

#dá pra checar também com mais de uma letra
print("tor" in nome)

#o not in verifica o inverso do in, caso ele esteja dentro da variável, vai retornar false
print("Vic" not in nome)

print(10 * "-")


nm = input("Digite seu nome: ")
en = input("Digite oque quer encontrar no seu nome: ")
if en in nm:
    print(f"{en} está em {nm}")
else:
    print(f"{en} não está em {nm}")