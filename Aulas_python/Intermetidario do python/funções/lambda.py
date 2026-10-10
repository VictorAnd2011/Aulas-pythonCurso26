# A função lambda é uma função como qualquer outra em Python
# Porém, são funções anônimas que contém apenas uma linha
# Ou seja, tudo deve ser contido dentro de uma única expressão.
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


#o sort deixa em ordem unicode, mas caso venha algo que ele não consiga ter ordem, tipo dics, ele dá erro
#ent temos que falar oq do dic ele vai ordenar
#então criamos uma funçãao para isso

# def ordem(item):
#     return item['nome']

# lista.sort(ordem)

#porém, não faz sentido criar um função de 1 linha só pra isso
#pra isso, criamos um func lambda, q tem apenas 1 linha e não pode ser usada novamente

lista.sort(key=lambda item: item['nome'])

for item in lista:
    print(item)