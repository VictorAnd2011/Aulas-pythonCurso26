x = 0.1
y = 0.7
print(x + y) #não dá exato 0.8, mas sim 0.7999999999999999
print(x + y == 0.8) #False
# a forma com que o python armazena os floats não é exata, então quando fazemos operações com eles, 
# o resultado pode não ser o esperado. Para contornar isso, 
# podemos usar a função round() para arredondar o resultado para um número específico de casas decimais.
print(round(x + y,1)) # 0.8
print(round(x + y,1) == 0.8) #True
