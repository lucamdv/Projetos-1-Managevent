import json

def carregar_eventos():
    try:
        with open("eventos.json", "r") as file:
            eventos = json.load(file)
    except FileNotFoundError:
        eventos = {}
    return eventos
def salvar_eventos(eventos):
    with open("eventos.json", "w") as file:
        json.dump(eventos, file)

def adicionar_evento(id_evento, nome, descricao, data, local):
    eventos = carregar_eventos()
    eventos[id_evento] = {
        "nome": nome,
        "descricao": descricao,
        "data": data,
        "local": local
    }
    salvar_eventos(eventos)
    print("Evento adicionado com sucesso!\n")

def listar_eventos():
    eventos = carregar_eventos()
    if eventos:
        for id_evento, evento in eventos.items():
            print(f"ID: {id_evento}")
            print(f"Nome: {evento['nome']}")
            print(f"Descrição: {evento['descricao']}")
            print(f"Data: {evento['data']}")
            print(f"Local: {evento['local']}")
            print("-----------------------")
    else:
        print("Não há eventos cadastrados.\n")

def atualizar_evento(id_evento, nome=None, descricao=None, data=None, local=None):
    eventos = carregar_eventos()
    if id_evento in eventos:
        if nome:
            eventos[id_evento]['nome'] = nome
        if descricao:
            eventos[id_evento]['descricao'] = descricao
        if data:
            eventos[id_evento]['data'] = data
        if local:
            eventos[id_evento]['local'] = local
        salvar_eventos(eventos)
        print("Evento atualizado com sucesso!\n")
    else:
        print("Evento não encontrado.")

def remover_evento(id_evento):
    eventos = carregar_eventos()
    if id_evento in eventos:
        del eventos[id_evento]
        salvar_eventos(eventos)
        print("Evento removido com sucesso!\n")
    else:
        print("Evento não encontrado.\n")

if __name__ == "__main__":
    while True:
        print("Bem vindo(a) ao portal de cadastro de eventos do Managevent!\n")
        print("1. Adicionar evento")
        print("2. Listar eventos")
        print("3. Atualizar evento")
        print("4. Remover evento")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_evento = input("Digite o ID do evento: ")
            nome = input("Digite o nome do evento: ")
            descricao = input("Digite a descrição do evento: ")
            data = input("Digite a data do evento: ")
            local = input("Digite o local do evento: ")
            adicionar_evento(id_evento, nome, descricao, data, local)
        elif opcao == "2":
            listar_eventos()
        elif opcao == "3":
            id_evento = input("Digite o ID do evento que deseja atualizar: ")
            nome = input("Digite o novo nome do evento (deixe em branco para manter o mesmo): ")
            descricao = input("Digite a nova descrição do evento (deixe em branco para manter a mesma): ")
            data = input("Digite a nova data do evento (deixe em branco para manter a mesma): ")
            local = input("Digite o novo local do evento (deixe em branco para manter o mesmo): ")
            atualizar_evento(id_evento, nome, descricao, data, local)
        elif opcao == "4":
            id_evento = input("Digite o ID do evento que deseja remover: ")
            remover_evento(id_evento)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

