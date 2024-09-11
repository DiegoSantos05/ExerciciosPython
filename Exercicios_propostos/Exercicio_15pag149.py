import random

# Preenchendo a matriz 10x10 com números inteiros aleatórios
matriz = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]

# Girar a matriz 90 graus no sentido horário
nova_matriz = []
for j in range(10):
    nova_linha = []
    for i in range(9, -1, -1):
        nova_linha.append(matriz[i][j])
    nova_matriz.append(nova_linha)

print("\nMatriz após girar 90 graus no sentido horário:")
for linha in nova_matriz:
    print("\t".join(map(str, linha)))

