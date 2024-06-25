"""Escreva um programa para aprovar um emprestimo bancario para compra de uma casa. O programa deve perguntar o valor da casa, o salario e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar"""

valor_casa = float(input("Digite o valor da casa a ser comprada "))
anos = float(input("Digite a quantidade de anos a pagar " ))
valor_salario = float(input("Digite o valor do seu salário " ))

meses = anos * 12

prestacao = valor_casa / meses
if prestacao <= (valor_salario * 0.30) :
    print(f"Prestação de R${prestacao:.2f} O seu salário é suficiente para a compra da casa")
elif prestacao > (valor_salario * 0.30) :
    print(f"Prestação de R${prestacao:.2f} O seu salário não é suficiente para a compra da casa")


