#Expressões algébricas
print("Soma de números inteiros")
print(1+2+3+4+5)
print("Cálculo de média")
print((23+19+31)/3)
print("Quantas vezes o número cabe dentro de outro")
print(403//73)
print("Somente o resto da divisão")
print(403%73)
print("Exponenciação")
print(2**10)
print("Valor absoluto entre números inteiros")
print(abs(54-57))
print("O menor valor entre números")
print(min(34, 29, 31), end="\n\n")

#Atribuições
print("Atribuir valores")
a = 3
b = 4
c = (a*a+b*b)
print(c)

#String
s1 = "ant"
s2 = "bat"
s3 = "cod"
print(s1 + ' ' + s2 + ' ' + s3)
print(10*(s1 + ' '))
print(s1 + ' ' + 2*(s2 + ' ')+ 3*(s3 + ' '))
print(7*(s1 + ' ' + s2 + ' '))
print(5*(s2 + s2 + s3 + ' '), end="\n\n")


print("Resolvendo problemas 02")
print("Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado")

km = float(input("Digite a quilometragem do carro: Km"))
dias = float(input("Digite a quantidade de dias em que usou o carro: "))

precokm = km * 0.15
precokm = round(precokm, 2)
precodia = dias * 60
total = precokm + precodia

print("O valor do aluguel por dia será de R${}, o valor do aluguel por Km percorrido será de R${}.".format(precokm, precodia))
print("O valor total será de R${}." .format(total))