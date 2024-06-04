import sys
import os
from time import sleep

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')



escolhas = {
    'local': None,
    'banda': None,
    'seguranca': None,
    'fotografia': None,
    'bar': None,
    'alimentacao': None
}

def menu_principal():
    while True:
        limpar()
        print("=" * 50)
        print("Escolha um Serviço que deseja contratar:")
        print("1. Locais")
        print("2. Bandas")
        print("3. Segurança")
        print("4. Fotografia")
        print("5. Bar")
        print("6. Alimentação")
        print("7. Sair")
        print("=" * 50)

        escolha = input("Digite o número do serviço desejado: ")

        if escolha == '1':
            escolha_local()
        elif escolha == '2':
            escolha_banda()
        elif escolha == '3':
            escolha_seguranca()
        elif escolha == '4':
            escolha_fotografia()
        elif escolha == '5':
            escolha_bar()
        elif escolha == '6':
            escolha_alimentacao()
        elif escolha == '7':
            limpar()
            print("Saindo do sistema, obrigado!")
            print("Suas escolhas:")
            
            for servico, escolha in escolhas.items():
                if escolha:
                    print(f"{servico.capitalize()}: {escolha}")
                    print("=" * 50)
            break
        else:
            print("Escolha Inválida")
            sleep(1)

def escolha_local():
    while True:
        limpar()
        print("Escolha um local:")
        print("1. Local 1")
        print("2. Local 2")
        print("3. Local 3")
        print("4. Voltar ao menu principal")

        escolha = input("Digite o numero do Local: ")

        if escolha == '1':
            escolhas['local'] = "Local 1"
        elif escolha == '2':
            escolhas['local'] = "Local 2"
        elif escolha == '3':
            escolhas['local'] = "Local 3"
        elif escolha == '4':
            return
        else:
            sleep(1)
            continue
        if perguntar_se_adicionar_outro():
            return

def escolha_banda():
    while True:
        limpar()
        print("=" * 50)
        print("Escolha uma banda:")
        print("1. Banda 1")
        print("2. Banda 2")
        print("3. Banda 3")
        print("4. Voltar ao menu principal")

        escolha = input("Digite o número da Banda: ")

        if escolha == '1':
            escolhas['banda'] = "Banda 1"
        elif escolha == '2':
            escolhas['banda'] = "Banda 2"
        elif escolha == '3':
            escolhas['banda'] = "Banda 3"
        elif escolha == '4':
            return
        else:
            sleep(1)
            continue
        if perguntar_se_adicionar_outro():
            return
        

def escolha_seguranca():
    while True:
        limpar()
        print("Escolha um serviço de segurança:")
        print("1. Segurança 1")
        print("2. Segurança 2")
        print("3. Segurança 3")
        print("4. Voltar ao menu principal")

        escolha = input("Digite o numero do Segurança: ")

        if escolha == '1':
            escolhas['seguranca'] = "Segurança 1"
        elif escolha == '2':
            escolhas['seguranca'] = "Segurança 2"
        elif escolha == '3':
            escolhas['seguranca'] = "Segurança 3"
        elif escolha == '4':
            return
        else:
            sleep(1)
            continue
        if perguntar_se_adicionar_outro():
            return

       
        

def escolha_fotografia():
    while True:
        limpar()
        print("Escolha um serviço de fotografia:")
        print("1. Fotografia 1")
        print("2. Fotografia 2")
        print("3. Fotografia 3")
        print("4. Voltar ao menu principal")

        escolha = input("Digite o numero do Serviço de Fotografia: ")

        if escolha == '1':
            escolhas['fotografia'] = "Fotografia 1"
        elif escolha == '2':
            escolhas['fotografia'] = "Fotografia 2"
        elif escolha == '3':
            escolhas['fotografia'] = "Fotografia 3"
        elif escolha == '4':
            return
        else:
            sleep(1)
            continue
        if perguntar_se_adicionar_outro():
            return

def escolha_bar():
    while True:
        limpar()
        print("Escolha um serviço de bar:")
        print("1. Bar 1")
        print("2. Bar 2")
        print("3. Bar 3")
        print("4. Voltar ao menu principal")

        escolha = input("Digite o numero do Bar: ")

        if escolha == '1':
            escolhas['bar'] = "Bar 1"
        elif escolha == '2':
            escolhas['bar'] = "Bar 2"
        elif escolha == '3':
            escolhas['bar'] = "Bar 3"
        elif escolha == '4':
            return
        else:
            sleep(1)
            continue
        if perguntar_se_adicionar_outro():
            return

def escolha_alimentacao():
    while True:
        limpar()
        print("Escolha um serviço de alimentação:")
        print("1. Alimentação 1")
        print("2. Alimentação 2")
        print("3. Alimentação 3")
        print("4. Voltar ao menu principal")

        escolha = input("Digite o numero do Serviço de Alimento: ")

        if escolha == '1':
            escolhas['alimentacao'] = "Alimentação 1"
        elif escolha == '2':
            escolhas['alimentacao'] = "Alimentação 2"
        elif escolha == '3':
            escolhas['alimentacao'] = "Alimentação 3"
        elif escolha == '4':
            return
        else:
            print("Digito invalido, tente novamente contratar o servico")
            return False
        if perguntar_se_adicionar_outro():
            return

def perguntar_se_adicionar_outro():
    while True:
        limpar()
        print("Deseja adicionar outro serviço?")
        print("1. Sim")
        print("2. Não, finalizar e sair")

        sub_escolha = input("Digite sua escolha: ")

        if sub_escolha == '1':
            return True
        elif sub_escolha == '2':
            limpar()
            print("Saindo do sistema, obrigado!")
            print("Suas escolhas:")
            for servico, escolha in escolhas.items():
                if escolha:
                    print(f"{servico.capitalize()}: {escolha}")
                    print("=" * 50)
            sys.exit()
        else:
            sleep(1)
            continue
                

menu_principal()