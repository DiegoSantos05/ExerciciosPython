def calcular_lucro(custo, preco):
    return ((preco - custo) / custo) * 100

produtos = []

for i in range(1, 51):
    nome = input(f"Digite o nome do produto {i}: ")
    custo = float(input(f"Digite o custo do produto {i}: "))
    preco = float(input(f"Digite o preço do produto {i}: "))
    produtos.append((nome, custo, preco))

lucro_menor_10 = []
lucro_entre_10_e_30 = []
lucro_maior_30 = []

for produto in produtos:
    nome, custo, preco = produto
    lucro = calcular_lucro(custo, preco)
    if lucro < 10:
        lucro_menor_10.append(produto)
    elif 10 <= lucro <= 30:
        lucro_entre_10_e_30.append(produto)
    else:
        lucro_maior_30.append(produto)

print("Produtos com lucro menor que 10%:")
for produto in lucro_menor_10:
    print(produto)

print("Produtos com lucro entre 10% e 30%:")
for produto in lucro_entre_10_e_30:
    print(produto)

print("Produtos com lucro maior que 30%:")
for produto in lucro_maior_30:
    print(produto)
