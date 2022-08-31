num1 = int(input("Digite um numero inteiro e positivo: "))
num2 = int(input("Digite outro numero inteiro e positivo: "))
print("Você deseja realizar qual operação matématica? ")
operacao = input("Digite: \n[1] para soma; \n[2] para subtração; \n[3] para multiplicar \n[4] para divisão: ")

if operacao == "1":
    soma = num1 + num2
    print(f"Você escolheu soma: {num1} + {num2} é {soma}")
elif operacao == "2":
    sub = num1 - num2
    print(f"Você escolheu subtração: {num1} - {num2} é {sub}")
elif operacao == "3":
    mult = num1 * num2
    print(f"Você escolheu multiplicação: {num1} x {num2} é {mult}")
elif operacao == "4":
    div = num1 / num2
    print(f"Você escolheu divisão: {num1}:{num2} é {div}")

