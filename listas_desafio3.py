lista = []
somapar = []
somaimpar = []
contador = 0

for contador in range(6):
    numeros= int(input(f"Adicione o {contador + 1}º número inteiro e positivo: "))
    if numeros == 0:
        print("não digite 0")
    else:
        while numero !=0:
            contador = contador + 1
            lista.append(numeros)
            if numeros %2 == 0:
                somapar.append(numeros)
            else:
               somaimpar.append(numeros)

print(f"A lista original\n{lista}")
print(f"A lista dos pares: {somapar}\nsoma dos pares: {sum(somapar)}")
print(f"A lista dos impares: {somaimpar}\nsoma dos impares: {sum(somaimpar)}")

#Precisa validar a condição de ser positivo!