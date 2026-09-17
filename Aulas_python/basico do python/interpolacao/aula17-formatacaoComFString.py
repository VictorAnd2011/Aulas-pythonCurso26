# .<n de digitos>f
# > -esquerda
# < - Direita
# ^ - centro
# sinal  - + ou -
# ex: 0>-100,.1f
# Conversion flags - !f !s !a

var = "abc"
print(f"{var}")
print(f"{var:->10}")#completa com o caracter anterior até chegar a 10, colocando na esquerda (como ja tinha 3 caracteres do abc, colocou 7 - para completar 10)
print(f"{var:_<10}")#coloca 7 + na direita para completar 10
print(f"{var:_^10}")#coloca mais 7 caracteres divididos ao meio para totalizar 10

print(f"{1067.5413653165}")
print(f"{1067.5413653165:.1f}")#limita para 1 casa decimal
print(f"{1067426.5413653165:,.1f}")#coloca virgula para cada 3 digitos
print(f"{1067426.5413653165:+,.1f}")#coloca o sinal do número, mesmo q ele seja positivo
print(f"{-1067426.5413653165:+,.1f}")#coloca -, mesmo que tenha colocado + na formatação
print(f"{1067:x}")#dá para transformar para exadecimal
print(f"{1067:08x}")#delimita uma quantidade de digitos padrão mínimo (só funciona com 0, e no hexadecimal)
print(f"{1067:08X}")#se usa X para deixar maísculo





