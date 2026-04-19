# # Cédulasx'

N = int(input())
valor = N
cedulas = [100,50,20,10,5,2,1]

print(N)
for nota in cedulas:
    quantidade = valor // nota
    valor %= nota

    print(f'{quantidade} nota(s) de R$ {nota},00')