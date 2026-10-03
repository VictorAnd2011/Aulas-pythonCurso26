'''
Dict são dados mutáveis
eles saõ criados usando {}

dicionarios são tipos listas, mas o indice vira um nome, e não um número
ex: pessoa = {
        'nome': 'Sabor',
        'sobrenome': 'Da Silva',
        'idade': 67,
        'altura': 1.67,
        'endereço': [
        {'rua': 'sabor das lagrimas', 'numero': 167},
        {'rua': 'rua dos ronaldos', 'numero': 442},
        ]
}
'''
pessoa = {
        'nome': 'Sabor',
        'sobrenome': 'Da Silva',
        'idade': 67,
        'altura': 1.67,
}

print(pessoa, type(pessoa)) 

print(pessoa['nome']) #mostra o valor do indice 'nome' do dicionario pessoa, como se fosse uma lista,
#mas com o indice sendo o nome do indice e não um número

for chave in pessoa:
    print(chave, pessoa[chave]) #mostra o nome do indice e o valor do indice do dicionario pessoa


#para criar uma chave nova, fazemos assim:
pessoa['peso'] = 67.5 #cria um novo indice 'peso'
print(pessoa['peso'])

#para apagar uma chave usamos o del
del pessoa['altura'] #apaga o indice 'altura'
print(pessoa)

#apagar chaves pode dar problemas,
#pois se tentarmos acessar um indice que não existe, o programa vai dar erro
#para evitar isso, podemos usar o metodo get, que retorna None (por padrão, mas pode mudar) 
#se o indice não existir
print(pessoa.get('altura')) #retorna None, pois o indice 'altura' não
print(pessoa.get('nome')) #retorna 'Sabor', pois o indice 'nome' existe
print(pessoa.get('altura', 'indice não existe')) #retorna oq eu escolhi