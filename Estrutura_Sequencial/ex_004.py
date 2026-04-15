# Faça um programa que peça as 4 notas bimestrais e mostre a média.
total = []

for i in range(4):
    notas = float(input(f'Digite a {i + 1} nota: '))
    total.append(notas)
media = sum(total) / 4
print(f'A média foi de {media:.2f}')        