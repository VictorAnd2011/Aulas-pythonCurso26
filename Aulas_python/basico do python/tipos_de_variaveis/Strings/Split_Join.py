'''
Split e Join
Split: Divide uma string em uma lista de substrings com base em um delimitador especificado
Join: Une uma lista de strings em uma única string com um delimitador especificado
'''

frase = 'Eu gosto do sabor energético'
frase_divida = frase.split()#quando não é especificado um delimitador, o padrão é o espaço em branco    
print(frase_divida)  # Saída: ['Eu', 'gosto', 'do', 'sabor', 'energético']

frase2 = 'O bora bill é legal, mas o Edinaldo Pereira é melhor!'
frase_divida2 = frase2.split(',')  # Especificando a vírgula como delimitador
print(frase_divida2)  # Saída: ['O bora bill é legal', ' mas o Edinaldo Pereira é melhor!']


#o join transforma uma lista de volta em str
frase_unida = ','.join(frase_divida2) #oq está entre aspas é oq vai separar os itens
frase_unida2 = ' SABOOOOOURR'.join(frase_divida2)
print(frase_unida) #Saída: 'O bora bill é legal mas o Edinaldo Pereira é melhor!'
print(frase_unida2) #Saída: 'O bora bill é legal SABOOOOOURR mas o Edinaldo Pereira é melhor!'
