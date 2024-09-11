# Criando uma matriz 5x5 preenchida com zeros
matriz = [[0] * 5 for _ in range(5)]

# Preenchendo a matriz com valores inteiros (você pode modificar os valores conforme necessário)
for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input(f"Digite o valor para a posição [{i+1}, {j+1}]: "))

# Exibindo a matriz original
print("Matriz original:")
for linha in matriz:
    print(linha)

matriz[1], matriz[4] = matriz[4], matriz[1]

for i in range(5):
    matriz[i][0], matriz[i][3] = matriz[i][3], matriz[i][0]

for i in range(5):
    matriz[i][i], matriz[i][4-i] = matriz[i][4-i], matriz[i][i]

print("Matriz após as trocas:")
for linha in matriz:
    print(linha)

