peso = float(input("Informe seu peso : "))
altura = float(input("Informe sua altura : "))
imc = float(peso / (altura ** 2))

if imc < 16:
    print(f"Seu imc é: {imc:.2f}. Baixo peso Grau III ")
elif 16 < imc < 16.9:
    print(f"Seu imc é: {imc:.2f}. Baixo peso Grau II ")
elif 17 < imc < 18.49:
    print(f"Seu imc é: {imc:.2f}. Baixo peso Grau I ")
elif 18.50 < imc < 24.99:
    print(f"Seu imc é: {imc:.2f}. Peso ideal  ")
elif 25 < imc < 29.99:
    print(f"Seu imc é: {imc:.2f}. Sobrepeso ")
elif 30 < imc < 34.99:
    print(f"Seu imc é: {imc:.2f}. Obesidade I ")
elif 35 < imc < 39.99:
    print(f"Seu imc é: {imc:.2f}. Obesidade II ")
elif imc >= 40:
    print(f"Seu imc é: {imc:.2f}. Obesidade III ")
