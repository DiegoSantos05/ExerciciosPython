# Inicialize as variáveis para contagem
total_entrevistados = 5
menor_18 = 0
entre_18_e_65 = 0
acima_de_65 = 0
excelente = 0
boa = 0
precisa_melhorar = 0
sugestoes = []

# Leia os dados da pesquisa
for _ in range(total_entrevistados):
    idade = int(input("Digite a idade do entrevistado: "))
    frequencia = int(input("Digite a frequência ao shopping (1-diária, 2-semanal, 3-eventual): "))
    avaliacao = int(input("Digite a avaliação da praça de alimentação (1-excelente, 2-boa, 3-precisa melhorar): "))
    
    # Contagem por faixa etária
    if idade < 18:
        menor_18 += 1
    elif idade <= 65:
        entre_18_e_65 += 1
    else:
        acima_de_65 += 1
    
    # Contagem das avaliações
    if avaliacao == 1:
        excelente += 1
    elif avaliacao == 2:
        boa += 1
    else:
        precisa_melhorar += 1
        sugestao = input("Digite a sugestão de melhoria: ")
        sugestoes.append((idade, sugestao))

# Cálculo das porcentagens
porcentagem_menor_18 = (menor_18 / total_entrevistados) * 100
porcentagem_entre_18_e_65 = (entre_18_e_65 / total_entrevistados) * 100
porcentagem_acima_de_65 = (acima_de_65 / total_entrevistados) * 100
porcentagem_excelente = (excelente / total_entrevistados) * 100
porcentagem_boa = (boa / total_entrevistados) * 100
porcentagem_precisa_melhorar = (precisa_melhorar / total_entrevistados) * 100

# Imprima os resultados
print(f"Porcentagem de entrevistados com menos de 18 anos: {porcentagem_menor_18:.2f}%")
print(f"Porcentagem de entrevistados entre 18 e 65 anos: {porcentagem_entre_18_e_65:.2f}%")
print(f"Porcentagem de entrevistados acima de 65 anos: {porcentagem_acima_de_65:.2f}%")
print(f"Porcentagem de avaliações excelentes: {porcentagem_excelente:.2f}%")
print(f"Porcentagem de avaliações boas: {porcentagem_boa:.2f}%")
print(f"Porcentagem de avaliações que precisam melhorar: {porcentagem_precisa_melhorar:.2f}%")

print("\nSugestões de melhoria:")
for idade, sugestao in sugestoes:
    print(f"Idade {idade}: {sugestao}")
