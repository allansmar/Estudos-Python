"""
Utilizando listas, como poderíamos escrever um
algoritmo que verificasse se uma palavra é um
PALÍNDROMO?
Exemplo de palíndromo: OVO, ANA, ARARA
(palavra que pode ser escrita da mesma forma iniciando
por qualquer um dos lados)
"""
print("VERIFICADOR DE PAlÍNDROMOS")
palavra = input("Digite uma palavra: ").upper()

lista = []
reversa = []

for letra in palavra:
    lista.append(letra)
    reversa.append(letra)

print(lista)
reversa.reverse()
print(reversa)

if lista == reversa:
    print(f"{palavra} é um PALÍNDROMO!")
else:
    print(f"{palavra} NÃO É um palíndromo.")