# Crie uma lista para armazenar os nomes dos participantes e outra para as pontuações
nomes = []
pontuacoes = []

# Leia os dados dos 200 participantes
for i in range(11):
    nome = input(f"Digite o nome do {i+190}º participante: ")
    pontuacao = float(input(f"Digite a pontuação final de {nome}: "))
    
    nomes.append(nome)
    pontuacoes.append(pontuacao)

# Crie uma lista com os índices dos participantes que obtiveram mais de 70 pontos
colocados = [i for i, pontuacao in enumerate(pontuacoes) if pontuacao > 70]

# Imprima o ranking dos colocados
print("\nRanking dos colocados com mais de 70 pontos:")
for i, indice in enumerate(colocados, start=1):
    print(f"{i}º lugar: {nomes[indice]} - {pontuacoes[indice]} pontos")


