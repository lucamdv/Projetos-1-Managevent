import json
import os

DATA_FILE = 'reclamacoes.json'

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

def read_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def write_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
        
def create_complaint():
    reclamacoes = read_data()
    nome_cliente = input("Digite o nome do cliente: ")
    email = input("Digite o email: ")
    assunto = input("Digite o assunto: ")
    descricao = input("Digite a descrição: ")
    nova_reclamacao = {
        'id': len(reclamacoes) + 1,
        'nome_cliente': nome_cliente,
        'email': email,
        'assunto': assunto,
        'descricao': descricao,
        'status': 'aberta'
    }
    reclamacoes.append(nova_reclamacao)
    write_data(reclamacoes)
    print("Reclamação criada com sucesso!")

def get_complaints():
    reclamacoes = read_data()
    for reclamacao in reclamacoes:
        print(json.dumps(reclamacao, indent=4))

def get_complaint():
    reclamacoes = read_data()
    id = int(input("Digite o ID da reclamação: "))
    reclamacao = next((rec for rec in reclamacoes if rec['id'] == id), None)
    if not reclamacao:
        print("Reclamação não encontrada")
    else:
        print(json.dumps(reclamacao, indent=4))

def update_complaint():
    reclamacoes = read_data()
    id = int(input("Digite o ID da reclamação: "))
    reclamacao = next((rec for rec in reclamacoes if rec['id'] == id), None)
    if not reclamacao:
        print("Reclamação não encontrada")
    else:
        nome_cliente = input(f"Digite o nome do cliente ({reclamacao['nome_cliente']}): ")
        email = input(f"Digite o email ({reclamacao['email']}): ")
        assunto = input(f"Digite o assunto ({reclamacao['assunto']}): ")
        descricao = input(f"Digite a descrição ({reclamacao['descricao']}): ")
        status = input(f"Digite o status ({reclamacao['status']}): ")
        if nome_cliente:
            reclamacao['nome_cliente'] = nome_cliente
        if email:
            reclamacao['email'] = email
        if assunto:
            reclamacao['assunto'] = assunto
        if descricao:
            reclamacao['descricao'] = descricao
        if status:
            reclamacao['status'] = status
        write_data(reclamacoes)
        print("Reclamação atualizada com sucesso!")

def delete_complaint():
    reclamacoes = read_data()
    id = int(input("Digite o ID da reclamação: "))
    reclamacao = next((rec for rec in reclamacoes if rec['id'] == id), None)
    if not reclamacao:
        print("Reclamação não encontrada")
    else:
        reclamacoes.remove(reclamacao)
        write_data(reclamacoes)
        print("Reclamação deletada com sucesso!")

def main():
    while True:
        print("\nSistema de Gestão de Reclamações")
        print("1. Criar reclamação")
        print("2. Ver todas as reclamações")
        print("3. Ver reclamação por ID")
        print("4. Atualizar reclamação")
        print("5. Deletar reclamação")
        print("6. Sair")
        escolha = input("Digite sua escolha: ")
        
        if escolha == '1':
            create_complaint()
        elif escolha == '2':
            get_complaints()
        elif escolha == '3':
            get_complaint()
        elif escolha == '4':
            update_complaint()
        elif escolha == '5':
            delete_complaint()
        elif escolha == '6':
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == '__main__':
    main()
