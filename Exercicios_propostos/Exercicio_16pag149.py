# Função para incluir um novo contato na lista
def incluir_contato(lista_contatos, nome_usual, nome_completo, telefone_fixo, telefone_celular):
    if len(lista_contatos) < 20:
        lista_contatos.append({
            'nome_usual': nome_usual,
            'nome_completo': nome_completo,
            'telefone_fixo': telefone_fixo,
            'telefone_celular': telefone_celular
        })
        print("Contato adicionado com sucesso!")
    else:
        print("A lista de contatos está cheia.")

# Função para consultar um contato pelo nome usual
def consultar_contato(lista_contatos, nome_usual):
    for contato in lista_contatos:
        if contato['nome_usual'] == nome_usual:
            print("Informações do Contato:")
            print("Nome Usual:", contato['nome_usual'])
            print("Nome Completo:", contato['nome_completo'])
            print("Telefone Fixo:", contato['telefone_fixo'])
            print("Telefone Celular:", contato['telefone_celular'])
            return
    print("Contato não encontrado.")

# Função para exibir todos os contatos em ordem alfabética pelo nome usual
def exibir_contatos(lista_contatos):
    lista_contatos.sort(key=lambda x: x['nome_usual'])
    print("Lista de Contatos:")
    for contato in lista_contatos:
        print("Nome Usual:", contato['nome_usual'])
        print("Nome Completo:", contato['nome_completo'])
        print("Telefone Fixo:", contato['telefone_fixo'])
        print("Telefone Celular:", contato['telefone_celular'])
        print()

# Lista para armazenar os contatos
contatos = []

# Loop para exibir o menu
while True:
    print("\nMenu de Opções:")
    print("0) Sair")
    print("1) Incluir um novo contato")
    print("2) Consultar um contato pelo nome usual")
    print("3) Exibir listagem de todos os contatos em ordem alfabética")

    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        print("Saindo do programa...")
        break
    elif opcao == '1':
        nome_usual = input("Digite o nome usual do contato: ")
        nome_completo = input("Digite o nome completo do contato: ")
        telefone_fixo = input("Digite o telefone fixo do contato: ")
        telefone_celular = input("Digite o telefone celular do contato: ")
        incluir_contato(contatos, nome_usual, nome_completo, telefone_fixo, telefone_celular)
    elif opcao == '2':
        nome_usual = input("Digite o nome usual do contato que deseja consultar: ")
        consultar_contato(contatos, nome_usual)
    elif opcao == '3':
        exibir_contatos(contatos)
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
