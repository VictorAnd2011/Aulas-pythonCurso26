'''
try - tenta executar um código
except -  executa o código caso de algum erro no try

'''

num_str = input("Digite um número para ser dobrado: ")

try: #Vai rodar esse código até dar algum erro
    print("str:",num_str)
    num_float = float(num_str) #Caso não tenha sido digitado um número, iria dar erro aqui, mas no caso ele apenas pula para o except
    print("Float:",num_float)
    print(f"Seu número dobrado é: {num_float * 2}")

except:
    print("vc não digitou um número") #se der erro, o código pula pra ca