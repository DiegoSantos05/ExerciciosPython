# Definindo a estrutura de dados para a agenda
agenda = {
    'segunda-feira': {'14h': 'livre', '15h': 'livre', '16h': 'livre', '17h': 'livre'},
    'terça-feira': {'14h': 'livre', '15h': 'livre', '16h': 'livre', '17h': 'livre'},
    'quarta-feira': {'14h': 'livre', '15h': 'livre', '16h': 'livre', '17h': 'livre'},
    'quinta-feira': {'14h': 'livre', '15h': 'livre', '16h': 'livre', '17h': 'livre'},
    'sexta-feira': {'14h': 'livre', '15h': 'livre', '16h': 'livre', '17h': 'livre'}
}

# Função para incluir uma nova consulta
def incluir_consulta():
    dia = input("Digite o dia da semana: ").lower()
    if dia in agenda:
        horario = input("Digite o horário da consulta (14h, 15h, 16h ou 17h): ")
        if horario in agenda[dia] and agenda[dia][horario] == 'livre':
            nome = input("Digite o nome do paciente: ")
            telefone = input("Digite o telefone do paciente: ")
            agenda[dia][horario] = {'nome': nome, 'telefone': telefone}
            print("Consulta agendada com sucesso!")
        else:
            print("Horário indisponível.")
    else:
        print("Dia inválido.")

# Função para remover uma consulta
def remover_consulta():
    dia = input("Digite o dia da semana (segunda-feira, terça-feira, etc.): ").lower()
    if dia in agenda:
        horario = input("Digite o horário da consulta (14h, 15h, 16h ou 17h): ")
        if horario in agenda[dia] and agenda[dia][horario] != 'livre':
            agenda[dia][horario] = 'livre'
            print("Consulta removida com sucesso!")
        else:
            print("Não há consulta marcada para este horário.")
    else:
        print("Dia inválido.")

# Função para exibir a lista completa da agenda
def exibir_agenda():
    for dia, horarios in agenda.items():
        print(f"{dia.capitalize()}:")
        for horario, consulta in horarios.items():
            if consulta == 'livre':
                print(f"\t{horario}: Livre")
            else:
                print(f"\t{horario}: {consulta['nome']} - {consulta['telefone']}")

# Loop para exibir o menu de opções
while True:
    print("\nMenu de Opções:")
    print("0) Sair")
    print("1) Incluir uma nova consulta")
    print("2) Remover uma consulta")
    print("3) Exibir a lista completa da agenda")

    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        print("Saindo do programa...")
        break
    elif opcao == '1':
        incluir_consulta()
    elif opcao == '2':
        remover_consulta()
    elif opcao == '3':
        exibir_agenda()
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
