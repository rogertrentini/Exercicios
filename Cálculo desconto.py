print("Resolvendo problemas 01")
print("Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto.", end="\n\n")

preco = float(input("Digite o valor de produto: R$"))
desconto = float(input("Digite o valor do desconto:"))
totaldesconto = preco * (desconto / 100)
totaldesconto = round(totaldesconto, 2)
valorfinal = preco - totaldesconto
print("O valor de seu produto é de R${}, seu desconto de {}%." .format(preco, desconto))
print("Valor desconto R${} e o valor final do produto R${}" .format(totaldesconto, valorfinal), end="\n\n\n")