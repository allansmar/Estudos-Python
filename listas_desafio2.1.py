lista = []
lista2 = []

for i in range(3):
    num = int(input("Adicione um número à lista: "))
    lista.append(num)

print(f"\n")
print(f"A lista original é: \n{lista}")

lista.sort()
print(f"A lista em ordem crescente é: \n{lista}")

lista.reverse()
print(f"A lista em ordem decrescente é: \n{lista}")