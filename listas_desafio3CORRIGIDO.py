lista = []
contador = 1

while contador <= 3:
    numero = int(input(f"Digite o {contador}º número: "))
    if numero > 0:
        lista.append(numero)
        contador = contador + 1
    elif numero == 0:
        print("Você digitou ZERO! Insira outro número!")
    else:
        print("Você digitou um número NEGATIVO! Insira outro número!")

pares = []
impares = []

for item in lista:
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)

print("A lista completa é:")
print(lista)
print("A lista dos números pares é:")
print(pares)
print("A lista dos números ímpares:")
print(impares)
print("A soma dos números pares é: ")
print(sum(pares))
print("A soma dos números ímpares: ")
print(sum(impares))