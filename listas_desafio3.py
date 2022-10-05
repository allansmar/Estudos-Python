lista = []
contador = 0
somapar = []
somaimpar = []

for contador in range(10):
    numeros= int(input(f"Adicione o {contador + 1}º número inteiro e positivo: "))
    if numeros %2 == 0:
        lista.append(somapar)
    elif numeros %2 != 0:
        lista.append(somaimpar)
    lista.append(numeros)
    contador = contador + 1

print(f"A soma dos pares é: {sum(somapar)}")
print(f"A soma dos impares é: {sum(somaimpar)}")
print(f"O menor é: {min(lista)}")
print(f"A lista: {lista}")