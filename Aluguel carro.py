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