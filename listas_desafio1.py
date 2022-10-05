lista = []
contador = 0

for contador in range(5):
    numeros= int(input(f"Adicione o {contador + 1}º número: "))
    lista.append(numeros)
    contador = contador + 1

print(f"A soma dos elementos da lista é: {sum(lista)}")
print(f"A média dos elementos da lista é: {sum(lista)/len(lista)}")
print(lista)


