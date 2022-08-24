#Questão 03 - Faça um programa que peça o raio de um círculo, calcule e mostre a
# sua área usando a biblioteca MATH.

import math
print("Vamos calcular a área do círculo ")
raio = float(input("Insira o raio do círculo: "))
area = float(raio ** 2) * math.pi
print(f'A área do círculo é: {area} m²')
