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
            espaco_usuário("CLIENTE")
        case 2:
            espaco_usuário("FORNECEDOR")
        case _:
            print("\nOpção inválida.")
            input("Pressione Enter para voltar...")
        

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

    codigo = None
    if perfil == "FORNECEDOR":
        codigo = input("Digite o código de identificação da sua empresa: ").strip()

    for cliente in dados:
        if cliente["cpf"] == cpf:
            print("Não foi possível realizar o seu cadastro. Este CPF já está cadastrado.")
            input("Pressione Enter para voltar...")
            return
    
    for cliente in dados:
        if cliente["email"] == email:
            print("Não foi possível realizar o seu cadastro. Esse E-mail já está cadastrado.")
            input("Pressione Enter para voltar...")
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
        "codigo" : codigo
    }

    dados.append(novo_cadastro)
    escrever_cadastro(dados)

    print(f"\n{nome}, seu cadastro foi realizado com sucesso: ")
    print("="*20)
    print(f"{perfil}")
    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    print(f"E-mail: {email}")
    print(f"Telefone: {telefone}")
    if perfil == "FORNECEDOR":
        print(f"Código: {codigo}")
    print("\n", "="*20)
    input("Pressione Enter para voltar...")

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


def escrever_dados_pagamento(pagamentos):
    if not pagamentos:
        pagamentos = []
    dados = ler_pagamento()
    with open('pagamento.json', 'w') as arquivo:
        json.dump(pagamentos, arquivo, indent=4)


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

    input("Pressione Enter para voltar...")


def espaco_usuário(perfil):
    os.system('cls')
    dados = ler_cadastro()
    print("="*5, end="")
    print("LOGIN", end="")
    print("="*5)
    cpf = input("CPF: ")
    senha = input("senha: ").strip()
    for cliente in dados:
        if cliente['cpf'] == cpf and cliente['senha'] == senha:
            if perfil == 'CLIENTE':
                pagina_cliente(cpf)
            else:
                pagina_fornecedor(cpf)
            return            
    
    continuar = input("Não encontrei o seu cadastro. Deseja tentar novamente? [S/N]: ").strip().lower()
    if continuar[0] == "s":
        return espaco_usuário(perfil)
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
    input("Pressione Enter para voltar...")
    return


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
    
    input("Pressione Enter para voltar...")
    return


def pagina_cliente(cpf):
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
        case '1':
            ver_perfil_cliente(cpf)
        case '2':
            alterar_perfil_cliente(cpf)
        case '3':
            cadastrar_pagamento_cliente(cpf)
        case '4':
            ver_pagamentos_cliente(cpf)
        case '5':
            apagar_perfil_cliente(cpf)
        case '6':
            return
        case _:
            print("Opção inválida. Tente novamente.")
            sleep(1)
            pagina_cliente(cpf)


def ver_perfil_cliente(cpf): #Finalizar
    os.system('cls')
    dados = ler_cadastro()
    for cliente in dados:
        if cliente['cpf'] == cpf:
            print("Seu perfil: ")
            print("="*10, end="")
            print(f"{cliente["nome"]}", end="")
            print("="*10)
            for chave, valor in cliente.items():
                print(f"{chave}: {valor}")
            print("="*25)
            input("Pressione Enter para voltar...")
            return pagina_cliente(cpf)


def alterar_perfil_cliente(cpf):
    os.system('cls')
    dados = ler_cadastro()
    for cliente in dados:
        if cliente['cpf'] == cpf:
            print("Alterando o seu perfil...\n")
            nome_novo = input(f"Nome: {cliente['nome']} --> Novo nome: ").strip()
            cliente['nome'] = nome_novo if nome_novo else cliente['nome']

            email_novo = input(f"E-mail: {cliente['email']} --> Novo e-mail: ").strip()
            cliente['email'] = email_novo if email_novo else cliente['email']

            telefone_novo = input(f"Telefone: {cliente['telefone']} --> Novo telefone: ").strip()
            cliente['telefone'] = telefone_novo if telefone_novo else cliente['telefone']

            nova_senha = input(f"Digite a nova senha (ou deixe em branco para manter a atual): ").strip()
            if nova_senha:
                confirmacao_senha = input("Confirme a nova senha: ").strip()
                while nova_senha != confirmacao_senha:
                    print("As senhas não conferem. Tente novamente")
                    nova_senha = input("Digite a nova senha: ").strip()
                    confirmacao_senha = input("Confirme a nova senha: ").strip()
                cliente['senha'] = nova_senha

            escrever_cadastro(dados)
            print("Perfil atualizado com sucesso!")
            input("Pressione Enter para voltar...")
            return pagina_cliente(cpf)
    print("Cliente não encontrado.")  


def cadastrar_pagamento_cliente(cpf):
    os.system('cls')
    dados = ler_cadastro()
    pagamentos = ler_pagamento()
    fornecedores = []
    for pessoa in dados:
        if pessoa['perfil'] == "FORNECEDOR":
            fornecedores.append(pessoa)
        
    if not fornecedores:
        print("Ainda não há fornecedores cadastrados")
        input("Pressione Enter para voltar...")
        return pagina_cliente(cpf)
    
    print("Fornecedores disponíveis: ")
    for id, pessoa in enumerate(fornecedores):
        codigo = pessoa.get('codigo', 'N/A')
        print(f"{id+1}. {pessoa["nome"]} Código: {codigo}")
    
    codigo_fornecedor = input("Digite o código do fornecedor: ")
    fornecedor_selecionado = None
    for fornecedor in fornecedores:
        if fornecedor['codigo'] == codigo_fornecedor:
            fornecedor_selecionado = fornecedor
            break

    if not fornecedor_selecionado:
        print("Fornecedor não encontrado. Tente novamente")
        input("Pressione Enter para voltar...")
        return pagina_cliente(cpf)
    
    valor = input("Digite o valor do pagamento: R$").strip()
    descricao = input("Descrição do pagamento: ").strip()

    novo_pagamento = {
        "cpf_cliente": cpf,
        "fornecedor_codigo": fornecedor_selecionado['codigo'],
        "valor": valor,
        "descricao": descricao,
        "status": "PENDENTE"

    }

    pagamentos.append(novo_pagamento)
    escrever_dados_pagamento(pagamentos)
    print("Pagamento cadastrado com sucesso!")
    input("Pressione Enter para voltar...")
    return pagina_cliente(cpf)


def ver_pagamentos_cliente(cpf): #Finalizar
    os.system('cls')
    pagamentos = ler_pagamento()
    print("Seus pagamentos cadastrados: ")
    for pagamento in pagamentos:
        if pagamento['cpf_cliente'] == cpf:
            print("="*10)
            print(f"Fornecedor: {pagamento["fornecedor_codigo"]}")
            print(f"Valor: R${pagamento["valor"]}")
            print(f"Descrição: {pagamento["descricao"]}")
            print(f"Status: {pagamento["status"]}")
            print("="*10)
    input("Pressione Enter para voltar...")
    return pagina_cliente(cpf)


def apagar_perfil_cliente(cpf):
    os.system('cls')
    confirmação = input("Deseja realmente apagar o seu perfil? (s/n): ").strip()
    if confirmação[0] == "s":
        dados = ler_cadastro()
        for cliente in dados:
            if cliente["cpf"] == cpf: 
                dados.remove(cliente)
                escrever_cadastro(dados)
                print("Seu perfil foi excluído com sucesso!")
                input("Pressione Enter para voltar...")
                return
    else:
        print("Exclusão de perfil cancelada.")
        input("Pressione Enter para voltar...")
        return pagina_cliente(cpf)


def pagina_fornecedor(cpf):
    os.system('cls')
    print("="*7, end="")
    print("FORNECEDOR", end="")
    print("="*7)
    print()
    print("1. Ver perfil")
    print("2. Alterar perfil")
    print("3. Ver todos os pagamentos cadastrados")
    print("4. Confirmar pagamentos")
    print("5. Apagar perfil")
    print("6. Voltar ao menu principal")
    escolha = input("Escolha uma opção: ")
    match(escolha):
        case '1':
            ver_perfil_fornecedor(cpf)
        case '2':
            alterar_perfil_fornecedor(cpf)
        case '3':
            dados = ler_cadastro()
            fornecedor_codigo = None
            for fornecedor in dados:
                if fornecedor['cpf'] == cpf and fornecedor['perfil'] == "FORNECEDOR":
                    fornecedor_codigo = fornecedor['codigo']
                    break
            if fornecedor_codigo:
                ver_pagamentos_fornecedor(cpf, fornecedor_codigo)
            else: 
                print("Fornecedor não encontrado")
                input("Pressione Enter para voltar...")
                return pagina_fornecedor(cpf)
            
        case '4':
            dados = ler_cadastro()
            fornecedor_codigo = None
            for fornecedor in dados:
                if fornecedor['cpf'] == cpf and fornecedor['perfil'] == "FORNECEDOR":
                    fornecedor_codigo = fornecedor['codigo']
                    break
            if fornecedor_codigo:
                confirmar_pagamento(cpf, fornecedor_codigo)
            else: 
                print("Fornecedor não encontrado")
                input("Pressione Enter para voltar...")
            return pagina_fornecedor(cpf)

            
        case '5':
            apagar_perfil_fornecedor(cpf)
        case '6':
            return
        case _:
            print("Opção inválida. Tente novamente")
            sleep(1)
            pagina_fornecedor(cpf)


def ver_perfil_fornecedor(cpf):
    os.system('cls')
    dados = ler_cadastro()
    for fornecedor in dados:
        if fornecedor["cpf"] == cpf and fornecedor['perfil'] == "FORNECEDOR":
            print("Perfil do fornecedor: ")
            print("="*10, end="")
            print(f"{fornecedor["nome"]}", end="")
            print("="*10)
            for chave, valor in fornecedor.items():
                print(f"{chave}: {valor}")
            print("="*25)
            input("Pressione Enter para voltar...")
            return pagina_fornecedor(cpf)
    print("Fornecedor não encontrado.")
    

def alterar_perfil_fornecedor(cpf):
    os.system('cls')
    dados = ler_cadastro()
    for fornecedor in dados:
        if fornecedor['cpf'] == cpf and fornecedor['perfil'] == "FORNECEDOR":
            print("Alterando o seu perfil...")
            fornecedor["nome"] == input(f"Nome: {fornecedor['nome']} --> Novo nome: ").strip()
            fornecedor['email'] == input(f"E-mail: {fornecedor['email']} --> Novo e-mail: ").strip()
            fornecedor['telefone'] == input(f"Telefone: {fornecedor["telefone"]} --> Novo Telefone: ").strip()
            nova_senha = input("Digite a nova senha (ou deixe em branco para manter a atual): ").strip()
            if nova_senha:
                confirmação_senha = input("Confirme a sua nova senha: ")
                while confirmação_senha != nova_senha:
                    print("As senhas não conferem. Tente novamente.")
                    nova_senha = input("Digite a nova senha: ")
                    confirmação_senha = input("Confirme a sua nova senha: ")
                fornecedor['senha'] = nova_senha
            escrever_cadastro(dados)
            print("Perfil atualizado com sucesso!")
            input("Pressione Enter para voltar...")
            return pagina_fornecedor(cpf)
    print("Fornecedor não encontrado.")


def ver_pagamentos_fornecedor(cpf, codigo):
    os.system('cls')
    pagamentos = ler_pagamento()
    print("Pagamentos feitos para esse fornecedor:")
    encontrou_pagamento = False
    for pagamento in pagamentos:
        if pagamento['fornecedor_codigo'] == codigo:
            encontrou_pagamento = True
            print("="*10)
            print(f"Cliente: {pagamento['cpf_cliente']}")
            print(f"Valor: R${pagamento['valor']}")
            print(f"Descrição: {pagamento['descricao']}")
            print(f"Status: {pagamento['status']}")
            print("="*10)
    if not encontrou_pagamento:
        print("Nenhum pagamento encontrado para este fornecedor.")
    input("Pressione Enter para voltar...")
    return pagina_fornecedor(cpf)


def confirmar_pagamento(cpf, fornecedor_codigo):
    os.system('cls')
    pagamentos = ler_pagamento()
    pendentes = []
    
    for pagamento in pagamentos:
        if pagamento['fornecedor_codigo'] == fornecedor_codigo and pagamento['status'] == "PENDENTE":
            pendentes.append(pagamento)
    
    if not pendentes:
        print("Não há pagamentos pendentes.")
        input("Pressione Enter para voltar...")
        return pagina_fornecedor(cpf)

    print("Pagamentos pendentes:")
    for id, pagamento in enumerate(pendentes):
        print("="*10)
        print(f"{id + 1}. Cliente: {pagamento['cpf_cliente']}")
        print(f"Valor: R${pagamento['valor']}")
        print(f"Descrição: {pagamento['descricao']}")
        print("="*10)
    

    escolha = int(input("Escolha um pagamento para confirmar pelo número: ").strip())
    if 1 <= escolha <= len(pendentes):
        pagamento = pendentes[escolha - 1]
        pagamento['status'] = "CONFIRMADO"
        escrever_dados_pagamento(pagamentos)
        print("Pagamento confirmado com sucesso.")
    else:
        print("Escolha inválida.")
    
    input("Pressione Enter para voltar...")
    return pagina_fornecedor(cpf)




def apagar_perfil_fornecedor(cpf):
    os.system('cls')
    confirmação = input("Deseja realmente apagar o seu perfil? (s/n): ").strip()
    if confirmação[0] == "s":
        dados = ler_cadastro()
        for fornecedor in dados:
            if fornecedor["cpf"] == cpf: 
                dados.remove(fornecedor)
                escrever_cadastro(dados)
                print("Seu perfil foi excluído com sucesso!")
                input("Pressione Enter para voltar...")
                return
            
        
    else:
        print("Exclusão de perfil cancelada.")
        input("Pressione Enter para voltar...")
        return pagina_fornecedor(cpf)





def main():
    while True:
        os.system('cls')
        nome_sistema()
        inicio_sistema()


if __name__ == '__main__':
    main()
