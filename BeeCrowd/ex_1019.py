#Conversão de Tempo

N = int(input())

horas = N // 3600
sobra = N % 3600
minutos = sobra // 60
segundos = sobra % 60

print(f'{horas}:{minutos}:{segundos}')