def intersecao_vetores(vetor1, vetor2):
    intersecao = []
    for elemento in vetor1:
        if elemento in vetor2 and elemento not in intersecao: 
            intersecao.append(elemento)
            return intersecao
        
vetor1 = []
vetor2 = []

print ("Preencha o Primeiro vetor")
for i in range(20):
    elemento = int(input(f"Digite o {i+1} elemento: "))
    vetor1.append(elemento)

print("Preencha o segundo vetor:")
for i in range(20):
    elemento = int(input(f"Digite o {i+1} elemento: "))
    vetor2.append(elemento)

resultado = intersecao_vetores(vetor1,vetor2)
print("A intersecao dos vetores é:", resultado) 