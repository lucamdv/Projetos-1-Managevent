import os
import json
from time import sleep

def nome_sistema():
    print()
    print("="*30)
    print("    CONTROLE DE PAGAMENTOS")


def inicio_sistema():
    print("="*30)
    print("1. Login")
    print("2. Cadastrar")
    print("3. Mostrar clientes cadastrados")
    print("4. Mostrar fornecedores cadastrados")
    print("5. Procurar cliente") 
    print("6. Procurar fornecedor") 
    print("7. Sair")
    print("="*30)
    opcao_inicio = int(input("O que deseja fazer?: "))
    match(opcao_inicio):
        case 1: 
            login()
        case 2:
            cadastro()
        case 3:
            mostrar_cadastros('CLIENTE')
        case 4:
            mostrar_cadastros('FORNECEDOR')
        case 5:
            procurar_cliente()
        case 6: 
            procurar_fornecedor()
        case 7:
            print("Encerrando...")
            sleep(1)
            print("Volte sempre!")
            exit()
        case _:
            print("Opção inválida!")
    sleep(1)


def identificar_perfil(cpf, senha):
    dados = ler_cadastro()
    for pessoa in dados:
        if pessoa['cpf'] == cpf and pessoa['senha'] == senha:
            return pessoa['perfil']


def login():
    os.system('cls')
    print("="*10, end="")
    print("LOGIN", end="")
    print("="*10)
    print("1. Cliente")
    print("2. Fornecedor")
    print("="*25)
    login = int(input("Por favor, se identifique: "))
    match(login):
        case 1:
            espaco_cliente()
        case 2:
            espaco_fornecedor()
        case _:
            print("\nOpção inválida.")
            sleep(1)
        

def cadastro():
    os.system('cls')
    dados = ler_cadastro()
    print("="*10)
    print(" CADASTRO")
    print("="*10)

    nome = input("Nome: ").strip()
    perfil = input("Cliente ou fornecedor? [C/F]: ").strip().lower()
    perfil = "FORNECEDOR" if perfil == "f" else "CLIENTE"
    cpf = input("CPF: ")
    while len(cpf) != 11:
        print("CPF inválido! Tente novamente.")
        cpf = input("CPF: ").strip()
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    senha = input("Senha: ").strip()
    confirmacao_senha = input("Digite novamente a sua senha para confirmação: ")

    for cliente in dados:
        if cliente["cpf"] == cpf:
            print("Não foi possível realizar o seu cadastro. Este CPF já está cadastrado.")
            return
    
    for cliente in dados:
        if cliente["email"] == email:
            print("Não foi possível realizar o seu cadastro. Esse E-mail já está cadastrado.")
            return

    while senha != confirmacao_senha:
        print("\nAs senhas não conferem! Tente novamente:")
        confirmacao_senha = input("Digite a senha para confirmação: ")

    novo_cadastro = {
        "perfil": perfil, 
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "telefone": telefone,
        "senha": senha,
    }

    dados.append(novo_cadastro)
    escrever_cadastro(dados)

    print(f"\n{nome}, seu cadastro foi realizado com sucesso: ")
    print("="*20)
    print(f"{perfil}")
    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    print(f"E-mail: {email}")
    print(f"Telefone: {telefone}\n")
    print("="*20)


def ler_cadastro():
    try:
        with open('cadastro.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []


def escrever_cadastro(dados):
    with open('cadastro.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)


def ler_pagamento():
    try: 
        with open('pagamento.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []


def escrever_dados_pagamento():
    dados = ler_pagamento()
    with open('pagamento.json', 'w') as arquivo:
        json.dump(dados, arquivo)


def mostrar_cadastros(tipo):
    os.system('cls')
    dados = ler_cadastro()
    if dados: 
        tipo_plural = 'fornecedores' if tipo == "FORNECEDOR" else "clientes"
        print(f"\nExibindo todos os {tipo_plural.lower()}s cadastrados:")
        for cliente in dados:
            if cliente['perfil'] == tipo:
                print()
                print("=" *10, end="")
                print(cliente['nome'], end="")
                print("=" *10)
                for chave, valor in cliente.items():
                    if chave != "senha":
                        print(f"{chave}: {valor}")
                print("=" * 30)
    else:
        print(f"Ainda não há {tipo.lower()} cadastrado")

    sleep(2)


def espaco_cliente():
    os.system('cls')
    dados = ler_cadastro()
    print("="*5, end="")
    print("LOGIN", end="")
    print("="*5)
    cpf = input("CPF: ")
    senha = input("senha: ").strip()
    for cliente in dados:
        if cliente['cpf'] == cpf and cliente['senha'] == senha:
            print("Achei voce!")
            pagina_cliente()
            return 
    
    continuar = input("Não encontrei o seu cadastro. Deseja tentar novamente? [S/N]: ").strip().lower()
    if continuar[0] == "s":
        return espaco_cliente()
    else:
        return


def espaco_fornecedor():
    os.system('cls')
    dados = ler_cadastro()
    print("="*10, end="")
    print("LOGIN", end="")
    print("="*10)
    cpf = input("CPF: ")
    senha = input("senha: ").strip()
    for cliente in dados:
        if cliente['cpf'] == cpf and cliente['senha'] == senha:
            print("Fornecedor encontrado")
            pagina_fornecedor()
            return 
    
    continuar = input("Não achei o seu cadastro. Deseja tentar novamente? [S/N]: ").strip().lower()
    if continuar[0] == "s":
        return espaco_fornecedor()
    else:
        return


def procurar_cliente():
    os.system('cls')
    dados = ler_cadastro()
    print("Digite o cpf do cliente que está procurando: ")
    cpf = input("CPF: ").strip()
    encontrado = False
    for cliente in dados:
        if cliente['cpf'] == cpf and cliente["perfil"] == "CLIENTE":
            print("\nCliente encontrado: \n")
            print("=" *10, end="")
            print(cliente['nome'], end="")
            print("=" *10)
            for chave, valor in cliente.items():
                if chave != "senha":
                    print(f"{chave}: {valor}")
            print("=" * 30)
            encontrado = True
            break
    if encontrado == False:
            print("Não consegui achar o cadastro desse cliente.")


def procurar_fornecedor():
    os.system('cls')
    dados = ler_cadastro()
    print("Digite o cpf do fornecedor que está procurando: ")
    cpf = input("CPF: ").strip()
    encontrado = False
    for cliente in dados:
        if cliente["cpf"] == cpf and cliente["perfil"] == "FORNECEDOR":
            print("\nCliente encontrado: \n")
            print("=" *10, end="")
            print(cliente['nome'], end="")
            print("=" *10)
            for chave, valor in cliente.items():
                if chave != "senha":
                    print(f"{chave}: {valor}")
            print("=" *30)
            encontrado = True
            break
    if encontrado == False:
        print("Não consegui achar o cadastro desse fornecedor.")


def pagina_cliente():
    os.system('cls')
    print("="*7, end="")
    print("CLIENTE", end="")
    print("="*7)
    print()
    print("1. Ver perfil")
    print("2. Alterar perfil")
    print("3. Cadastrar pagamento")
    print("4. Ver todos os pagamentos")
    print("5. Apagar perfil")
    print("6. Voltar ao menu principal")
    escolha = input("Escolha uma opção: ")
    match(escolha):
        case 1:
            ver_perfil()
        case 2:
            alterar_perfil()
        case 3:
            cadastrar_pagamento()
        case 4:
            ver_pagamentos()
        case 5:
            apagar_perfil()
        case 6:
            inicio_sistema()
        case _:
            print("Opção inválida. Tente novamente.")
            sleep(1)
            pagina_cliente()
            
    


def pagina_fornecedor():
    print()

def pagamentos(): #Aqui será mostrada todos os pagamentos do cliente que fez o login
    os.system('cls') 
    print("Aqui estão os seus cadastros de pagamentos!")


def fornecimento(): #Aqui será mostrada todas os produtos fornecidos pelo fornecedor do login
    os.system('cls')
    print("Aqui estão os seus cadastros de formecimento!")


def ver_perfil():
    print("Vendo seu perfil")


def alterar_perfil():
    print("Alterando seu perifl")


def cadastrar_pagamento():
    print("Cadastrando o seu perfil")


def ver_pagamentos():
    print("Vendo seus pagamentos")


def apagar_perfil():
    print("Apagando o seu perfil")



def main():
    nome_sistema()
    while True:
        inicio_sistema()


if __name__ == '__main__':
    main()