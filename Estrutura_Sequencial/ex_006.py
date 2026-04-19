#Faça um programa que peça o raio de um círculo, calcule e mostre sua área:
import math

raio = float(input('Digite o valor do raio: '))
area = math.pi * (raio ** 2)
print(f'O valor da área é de: {area:.2f}')