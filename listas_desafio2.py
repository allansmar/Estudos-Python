lista = []
contador = 0

for contador in range(3):
    numeros= int(input(f"Adicione o {contador + 1}º número: "))
    lista.append(numeros)
    contador = contador + 1


print(f"O maior é: {max(lista)}")
print(f"O menor é: {min(lista)}")
print(f"A lista: {lista}")