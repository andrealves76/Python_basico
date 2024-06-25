"""Escreva um programa que leia dois numeros e que pergunte qual operação você deseja realizar.Você deve calcular soma, subtração, multiplicação ou divisão.Exiba o resultado da operação solicitada"""

primeiro_numero = int(input("Digite o primeiro número da operação: "))
segundo_numero = int(input("Digite o segundo número da operação: "))
operacao = input("Qual operação você deseja realizar? Ecolha:( 1 para soma ), (2 para subtração) , (3 para multiplicação) ou (4 para divisão)")

resultado = 0

if operacao =="1":
    resultado = primeiro_numero + segundo_numero
elif operacao =="2":
    resultado = primeiro_numero - segundo_numero
elif operacao == "3":
    resultado = primeiro_numero * segundo_numero
elif operacao == "4":
    resultado = primeiro_numero / segundo_numero
else:
    print("Digite uma operação válida")
                 
    


print(f"O resultado da operação é {resultado}")
