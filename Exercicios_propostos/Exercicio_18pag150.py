class Veiculo:
    def __init__(self, proprietario, combustivel, modelo, cor, ano, placa):
        self.proprietario = proprietario
        self.combustivel = combustivel
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.placa = placa

def ler_veiculos():
    veiculos = []
    for _ in range(20):
        proprietario = input("Digite o nome do proprietário: ")
        combustivel = input("Digite o tipo de combustível (alcool, gasolina ou flex): ")
        modelo = input("Digite o modelo do veículo: ")
        cor = input("Digite a cor do veículo: ")
        ano = int(input("Digite o ano do veículo: "))
        placa = input("Digite a placa do veículo (exemplo: ABC1234): ")
        veiculos.append(Veiculo(proprietario, combustivel, modelo, cor, ano, placa))
    return veiculos

def listar_veiculos(veiculos):
    print("\nVeículos do condomínio:")
    for i, veiculo in enumerate(veiculos, start=1):
        print(f"{i}. Proprietário: {veiculo.proprietario}, Placa: {veiculo.placa}, Ano: {veiculo.ano}")

def listar_carros_ano_anterior(veiculos):
    print("\nCarros do ano 2000 ou anterior e que são flex:")
    for veiculo in veiculos:
        if veiculo.ano <= 2000 and veiculo.combustivel == "flex":
            print(f"Proprietário: {veiculo.proprietario}, Placa: {veiculo.placa}, Vaga: {veiculos.index(veiculo) + 1}")

def ordenar_por_ano_descendente(veiculos):
    print("\nCarros ordenados por ano (do mais novo para o mais antigo):")
    veiculos_ordenados = sorted(veiculos, key=lambda x: x.ano, reverse=True)
    for veiculo in veiculos_ordenados:
        print(f"Modelo: {veiculo.modelo}, Placa: {veiculo.placa}, Cor: {veiculo.cor}, Proprietário: {veiculo.proprietario}")

def trocar_veiculo(veiculos):
    vaga = int(input("Digite o número da vaga a ser ocupada (1 a 20, ou 0 para sair): "))
    if vaga == 0:
        return
    elif 1 <= vaga <= 20:
        veiculo = veiculos[vaga - 1]
        print(f"Vaga {vaga} ocupada por:")
        print(f"Proprietário: {veiculo.proprietario}, Modelo: {veiculo.modelo}, Placa: {veiculo.placa}")
        print("Digite os dados do novo veículo:")
        proprietario = input("Nome do proprietário: ")
        combustivel = input("Tipo de combustível (alcool, gasolina ou flex): ")
        modelo = input("Modelo do veículo: ")
        cor = input("Cor do veículo: ")
        ano = int(input("Ano do veículo: "))
        placa = input("Placa do veículo (exemplo: ABC1234): ")
        veiculos[vaga - 1] = Veiculo(proprietario, combustivel, modelo, cor, ano, placa)
        print("Veículo atualizado com sucesso!")
    else:
        print("Vaga inválida.")

def main():
    veiculos = ler_veiculos()
    listar_veiculos(veiculos)
    listar_carros_ano_anterior(veiculos)
    ordenar_por_ano_descendente(veiculos)
    while True:
        trocar_veiculo(veiculos)

if __name__ == "__main__":
    main()
