"""
=======================================================================

Solicite ao usuário que informe notas enquanto desejar
e, ao final,
informe a soma
e média das notas digitadas.

Imprima também todas as notas digitadas.

=======================================================================

listanotas = []
contador = 0

while True:
    decisao = input("Inserir nota? S/N: ")
    if decisao == "S" or "s":
        nota = int(input(f"Digite a {contador +1}ª nota: " ))
        contador = contador +1
        listanotas.append(nota)
    elif decisao == "N" or "n":
         print(f"Média: {sum(nota)/len(listanotas)} ")
    else:
        continue

print(f"Notas digitadas: {listanotas}")
print(f"{sum(nota)}")
print(f"")
print(f"Média: {sum(nota) / len(listanotas)} ")


"""




notas = []
contador = 1

while True:
    nota = int(input(f"Informe a {contador}ª nota: "))
    pergunta = int(input("Deseja adicionar outra nota?\n[1] - SIM\n[2] = NÃO\n"))
    if pergunta == 1:
        notas.append(nota)
        contador = contador + 1
    elif pergunta == 2:
        notas.append(nota)
        break
    else:
        print("Opção inválida! Digite novamente!")

print(notas)
print(f"A soma é {sum(notas)}.")
print(f"A média é {sum(notas)/len(notas)}.")







