# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados de iteráveis.
# - Seus valores serão sempre únicos;
l1 = [1,2,3,3,3,3,3,3,3,3,1,2,4]
print(f'{l1=}')
s1 = set(l1)
l2 = list(s1)
print(f'{l2=}')

# - Não aceitam valores mutáveis;
# s1 = {1,2,[1,2,3]} não aceita, pois tem uma lista (valor mutável)
s1 = {1,2,(1,2,3,)} #aceita, pois é um valor imutável
print(f'{s1=}')


# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard
s1.add(3) #só adiciona 1 por vez
print(f'{s1=}')

s1.update('Hello World', 1, 2, 3, 67) #caso eu passe apenas a str, ele vai iterar ela, como no caso tem uma tupla, não acontece isso
print(f'{s1=}')

s1.discard('Hello World') #para remover, como cada valor só tem 1 dele, dá pra fazer isso

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos