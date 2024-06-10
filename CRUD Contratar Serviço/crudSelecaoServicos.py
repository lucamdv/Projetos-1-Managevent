import os
import json

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def inicializar_escolhas():
    return {
        'local': None,
        'banda': None,
        'seguranca': None,
        'fotografia': None,
        'bar': None,
        'alimentacao': None
    }

def salvar_escolhas(escolhas):
    with open('escolhas.json', 'w') as f:
        json.dump(escolhasServicos, f, indent=4)

escolhasServicos = inicializar_escolhas()
salvar_escolhas(escolhasServicos)

servicos_opcoes = {
    'local': ["Local 1", "Local 2", "Local 3"],
    'banda': ["Banda 1", "Banda 2", "Banda 3"],
    'seguranca': ["Segurança 1", "Segurança 2", "Segurança 3"],
    'fotografia': ["Fotografia 1", "Fotografia 2", "Fotografia 3"],
    'bar': ["Bar 1", "Bar 2", "Bar 3"],
    'alimentacao': ["Alimentação 1", "Alimentação 2", "Alimentação 3"]
}

def menu_principal():
    while True:
        limpar()
        print("=" * 50)
        print("Escolha um Serviço que deseja contratar:")
        for idx, servico in enumerate(servicos_opcoes.keys(), 1):
            print(f"{idx}. {servico.capitalize()}")
        print("7. Ver escolhas salvas")
        print("8. Sair")
        print("=" * 50)

        escolha = input("Digite o número do serviço desejado: ")

        if escolha in [str(i) for i in range(1, 7)]:
            tipo_servico = list(servicos_opcoes.keys())[int(escolha) - 1]
            escolha_servico(tipo_servico)
            if not perguntar_se_adicionar_ou_finalizar():
                break
        elif escolha == '7':
            limpar()
            mostrar_escolhas()
            if not perguntar_se_voltar_ao_menu():
                break
        elif escolha == '8':
            limpar()
            mostrar_escolhas()
            salvar_escolhas(escolhasServicos)
            print("Saindo do sistema, obrigado!")
            break
        else:
            print("Escolha Inválida")
            input("Pressione Enter para continuar...")

def escolha_servico(tipo):
    while True:
        limpar()
        print(f"Escolha um(a) {tipo}:")
        for idx, opcao in enumerate(servicos_opcoes[tipo], 1):
            print(f"{idx}. {opcao}")
        print("4. Voltar ao menu principal")

        escolha = input(f"Digite o número do(a) {tipo}: ")

        if escolha in [str(i) for i in range(1, len(servicos_opcoes[tipo]) + 1)]:
            escolhasServicos[tipo] = servicos_opcoes[tipo][int(escolha) - 1]
            print(f"Você escolheu {escolhasServicos[tipo]}.")
            salvar_escolhas(escolhasServicos)
            return  
        elif escolha == '4':
            return
        else:
            print("Escolha inválida")
            input("Pressione Enter para continuar...")

def perguntar_se_adicionar_ou_finalizar():
    while True:
        limpar()
        print("Deseja adicionar outro serviço ou finalizar o programa?")
        print("1. Adicionar outro serviço")
        print("2. Finalizar e sair")

        sub_escolha = input("Digite sua escolha: ")

        if sub_escolha == '1':
            return True  
        elif sub_escolha == '2':
            limpar()
            print("Saindo do sistema, obrigado!")
            mostrar_escolhas()
            salvar_escolhas(escolhasServicos)
            return False  
        else:
            print("Escolha inválida")
            input("Pressione Enter para continuar...")

def perguntar_se_voltar_ao_menu():
    while True:
        print("Deseja voltar ao menu principal ou finalizar o programa?")
        print("1. Voltar ao menu principal")
        print("2. Finalizar e sair")

        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            return True
        elif escolha == '2':
            return False
        else:
            print("Escolha inválida")
            input("Pressione Enter para continuar...")

def mostrar_escolhas():
    print("Suas escolhas:")
    for servico, escolha in escolhasServicos.items():
        if escolha:
            print(f"{servico.capitalize()}: {escolha}")
        else:
            print(f"{servico.capitalize()}: Nenhuma escolha feita")
    print("=" * 50)

menu_principal()
