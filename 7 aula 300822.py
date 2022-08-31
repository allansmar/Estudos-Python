soma = 0
contador = 1

while contador <=5:
    numero = int(input(f"Digite o {contador}° numero: "))
    contador = contador +1
    soma = soma + numero
print(f"A soma é {soma}")