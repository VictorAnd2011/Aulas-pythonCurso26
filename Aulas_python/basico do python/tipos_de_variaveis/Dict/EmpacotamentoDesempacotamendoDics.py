pessoas = {
    'nome':'Sabor',
    'sobrenome':'Da Silva',
    # 'idade':67,
    # 'altura':1.67,
    # 'peso':67
}

a, b = pessoas #dá as chaves
print(a,b)

a,b = pessoas.values() #retorna os valores
print(a,b)

a,b = pessoas.items() #retorna as chaves e os valores como tuplas
print(a,b)
list(a,b)

(a1,a2),b = pessoas #retorna a chave para a1, e o valor para a2
print(a,b)