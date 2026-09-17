a = "sabor"
b = "bora bill"
c = 67.42

#format é um método usado para inserir valores e variáveis dentro de strings de forma organizada
#O método .format() substitui chaves {} vazias ou numeradas dentro de uma string pelos valores passados como argumentos
formato = 'o a é {}, o b é {}, o c é {}'.format(a, b, c)
print(formato)

#usando essas formas, pode-se colocar os valores em qualquer ordem
#o format pode ser posicional
print('eu gosto de {2}, de {0}, mas não de {1}'.format(a, b, c))
#ou nomeado (se for nomeado, todos os parametros a frente também tem que ser nomeados)
print('eu me chamo {nome}, eu irrito o {irritado}, usando {trem}'.format(nome=b, irritado=a, trem=c))