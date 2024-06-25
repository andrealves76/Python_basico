"""Escreva um programa que calcule o preço a pagar pelo fornecimento de energia eletrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residencial e I para industrial e C para comercio. Calcule o valor a pagar de acordo com a tabela:"""
# Residencial consumo até 500 kwh R$ 0,40 === acima de 500kwh R$ 0,65
# Comercial consumo até 1000 kwh R$ 0,55 === acima de 1000 kwh R$ 0,60
# industrial consumo de até 5000 kwh R$ 0,55 === acima de 5000 kwh R$ 0,60

kwh = float(input("Qual o quantidade de kWh consumidas? "))
tipo_instalacao = int(input("Qual o tipo de instalação: Digite (1) residencial (2) comercial (3) industrial "))

tarifa = 0
valor_pagar = 0

if tipo_instalacao == 1 and kwh <= 500:
    valor_pagar = kwh * 0.40
elif tipo_instalacao == 1 and kwh > 500:
    valor_pagar = kwh * 0.65
elif tipo_instalacao == 2 and kwh <= 1000:
    valor_pagar = kwh * 0.55
elif tipo_instalacao == 2 and kwh > 1000:
    valor_pagar = kwh * 0.60
elif tipo_instalacao == 3 and kwh <= 5000:
    valor_pagar = kwh * 0.55
else:
    valor_pagar = kwh * 0.60

print(f"O valor a pagar pela instalação {tipo_instalacao} é de R$ {valor_pagar:.2f} ")                    
