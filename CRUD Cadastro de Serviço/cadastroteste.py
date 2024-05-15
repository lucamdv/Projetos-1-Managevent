import os
import json
from time import sleep

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_servicos_bebidas():
    if os.path.exists('servicos_bebidas.json'):
        with open('servicos_bebidas.json', 'r') as file:
            return json.load(file)
    else:
        return {}

def salvar_servicos_bebidas(servicos_bebidas):
    with open('servicos_bebidas.json', 'w') as file:
        json.dump(servicos_bebidas, file, indent=4)

def carregar_servicos_buffet():
    if os.path.exists('servicos_buffet.json'):
        with open('servicos_buffet.json', 'r') as file:
            return json.load(file)
    else:
        return {}

def salvar_servicos_buffet(servicos_buffet):
    with open('servicos_buffet.json', 'w') as file:
        json.dump(servicos_buffet, file, indent=4)

def carregar_local_evento():
    if os.path.exists('local_evento.json'):
        with open('local_evento.json', 'r') as file:
            return json.load(file)
    else:
        return {}
    
def salvar_local_evento(local_evento):
    with open('local_evento.json', 'w') as file:
        json.dump(local_evento, file, indent=4)

def carregar_banda_artista():
    if os.path.exists('artista.json'):
        with open('artista.json', 'r') as file:
            return json.load(file)
    else:
        return {}

def salvar_banda_artista(banda_artista):
    with open('artista.json', 'w') as file:
        json.dump(banda_artista, file, indent=4)

def carregar_servicos_seguranca():
    if os.path.exists('seg.json'):
        with open('seg.json', 'r') as file:
            return json.load(file)
    else:
        return {}

def salvar_servicos_seguranca(servicos_seguranca):
    with open('seg.json', 'w') as file:
        json.dump(servicos_seguranca, file, indent=4)

def carregar_servicos_fotografia():
    if os.path.exists('fotografia.json'):
        with open('fotografia.json', 'r') as file:
            return json.load(file)
    else:
        return {}

def salvar_servicos_fotografia(servicos_fotografia):
    with open('fotografia.json', 'w') as file:
        json.dump(servicos_fotografia, file, indent=4)

def atualizar_valor_json(arquivo_json, estrutura, valor_antigo, novo_valor):
    with open(arquivo_json, 'r') as arquivo:
        dados = json.load(arquivo)
    
    chave_encontrada = False
    for item in dados[estrutura]:
        for chave, valor in item.items():
            if valor == valor_antigo:
                item[chave] = novo_valor
                chave_encontrada = True
                print(f"Valor antigo '{valor_antigo}' substituído por '{novo_valor}' com sucesso!.")
    
    if not chave_encontrada:
        print("Valor antigo não encontrado. Nenhuma modificação feita.")
    
    with open(arquivo_json, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def excluir_valor_json(arquivo_json, estrutura, valor):
    with open(arquivo_json, 'r') as arquivo:
        dados = json.load(arquivo)
    
    for item in dados[estrutura]:
        if valor in item.values():
            dados[estrutura].remove(item)  
            with open(arquivo_json, 'w') as arquivo:
                json.dump(dados, arquivo, indent=4)
            print(f"'{valor}' foi removido com sucesso!.")
            return
    
    print(f"Valor '{valor}' não encontrado. Nenhuma modificação feita.")

def excluir_elemento_json(arquivo_json, estrutura, indice):
    with open(arquivo_json, 'r') as arquivo:
        dados = json.load(arquivo)
    
    if 0 <= indice < len(dados[estrutura]):
        del dados[estrutura][indice]  
        with open(arquivo_json, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)
        print(f"Elemento {indice} removido com sucesso!.")
    else:
        print("Índice inválido. Nenhuma modificação feita.")

def limpar_array_json(arquivo_json, estrutura):
    with open(arquivo_json, 'r') as arquivo:
        dados = json.load(arquivo)
    
    for item in dados[estrutura]:
        for chave in item.keys():
            item[chave] = ""  
    
    with open(arquivo_json, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def menuprincipal():
    limpar()
    print("=====================================")
    print('Que serviço você deseja cadastrar? ')
    print('1- Local para evento')
    print('2- Serviço de Bebidas')
    print('3- Serviço de Buffet')
    print('4- Bandas e Artistas')
    print('5- Segurança (Bombeiros, Paramédicos, Vigilância)')
    print('6- Fotografia')
    print('7- Atualizar meu serviço')
    print('8- Excluir meu serviço')
    print('9- Mostrar serviços cadastrados')
    print ('10- Finalizar')
    print("=====================================")
    global codigo
    codigo = int(input('\nDigite o código do que deseja: '))

def voltamenu():
    input('Digite qualquer tecla para voltar ao menu principal')
    main()

def escolhas():

    match(codigo):

        case 1:
            limpar()
            
            locais = carregar_local_evento()
            novo_local = {}
            novo_local["nome_local"] = input('Nome do Local: ')
            novo_local["endereco"] = input('Endereço: ')
            novo_local["cidade"] = input('Cidade: ')
            novo_local["estado_provincia"] = input('Estado/Província: ')
            novo_local["cep"] = input('CEP: ')
            novo_local["telefone_contato"] = input('Telefone de Contato: ')
            novo_local["email_contato"] = input('E-mail de Contato: ')
            novo_local["tipo_local"] = input('Tipo de Local: ')
            novo_local["descricao_local"] = input('Descrição do Local: ')
            novo_local["horario_funcionamento"] = {}
            novo_local["horario_funcionamento"]["segunda-feira"] = input('Horário de Funcionamento - Segunda-feira: ')
            novo_local["horario_funcionamento"]["terca-feira"] = input('Horário de Funcionamento - Terça-feira: ')
            novo_local["horario_funcionamento"]["quarta-feira"] = input('Horário de Funcionamento - Quarta-feira: ')
            novo_local["horario_funcionamento"]["quinta-feira"] = input('Horário de Funcionamento - Quinta-feira: ')
            novo_local["horario_funcionamento"]["sexta-feira"] = input('Horário de Funcionamento - Sexta-feira: ')
            novo_local["horario_funcionamento"]["sabado"] = input('Horário de Funcionamento - Sábado: ')
            novo_local["horario_funcionamento"]["domingo"] = input('Horário de Funcionamento - Domingo: ')
            locais["locais"].append(novo_local)

            salvar_local_evento(locais)
            voltamenu()

        case 2:

            limpar()
            bebidas = carregar_servicos_bebidas()
            novo_servico_bebidas = {}
            novo_servico_bebidas["nome_servico"] = input('Nome do Serviço: ')
            novo_servico_bebidas["endereco"] = input('Endereço: ')
            novo_servico_bebidas["cidade"] = input('Cidade: ')
            novo_servico_bebidas["estado_provincia"] = input('Estado/Província: ')
            novo_servico_bebidas["cep"] = input('CEP: ')
            novo_servico_bebidas["telefone_contato"] = input('Telefone de Contato: ')
            novo_servico_bebidas["email_contato"] = input('E-mail de Contato: ')
            novo_servico_bebidas["tipo_servico_bebidas"] = input('Tipo de Serviço de Bebidas: ')
            novo_servico_bebidas["descricao_servico"] = input('Descrição do Serviço: ')
            novo_servico_bebidas["tipos_bebidas_oferecidas"] = input('Tipos de Bebidas Oferecidas (separadas por vírgula): ').split(',')
            novo_servico_bebidas["horario_funcionamento"] = {}
            novo_servico_bebidas["horario_funcionamento"]["segunda-feira"] = input('Horário de Funcionamento - Segunda-feira: ')
            novo_servico_bebidas["horario_funcionamento"]["terca-feira"] = input('Horário de Funcionamento - Terça-feira: ')
            novo_servico_bebidas["horario_funcionamento"]["quarta-feira"] = input('Horário de Funcionamento - Quarta-feira: ')
            novo_servico_bebidas["horario_funcionamento"]["quinta-feira"] = input('Horário de Funcionamento - Quinta-feira: ')
            novo_servico_bebidas["horario_funcionamento"]["sexta-feira"] = input('Horário de Funcionamento - Sexta-feira: ')
            novo_servico_bebidas["horario_funcionamento"]["sabado"] = input('Horário de Funcionamento - Sábado: ')
            novo_servico_bebidas["horario_funcionamento"]["domingo"] = input('Horário de Funcionamento - Domingo: ')
            novo_servico_bebidas["faixa_preco"] = input('Faixa de Preço: ')
            novo_servico_bebidas["redes_sociais_website"] = {}
            novo_servico_bebidas["redes_sociais_website"]["instagram"] = input('Instagram: ')
            novo_servico_bebidas["redes_sociais_website"]["website"] = input('Website: ')
            novo_servico_bebidas["open_bar"] = input('Open Bar (Sim/Não): ')
            bebidas['bebidas'].append(novo_servico_bebidas)

            salvar_servicos_bebidas(bebidas)
            voltamenu()

        case 3:
            limpar()
            buffet = carregar_servicos_buffet()
            novo_servico_buffet = {}
            novo_servico_buffet["nome_servico_buffet"] = input('Nome do Serviço de Buffet: ')
            novo_servico_buffet["endereco"] = input('Endereço: ')
            novo_servico_buffet["cidade"] = input('Cidade: ')
            novo_servico_buffet["estado_provincia"] = input('Estado/Província: ')
            novo_servico_buffet["cep"] = input('CEP: ')
            novo_servico_buffet["telefone_contato"] = input('Telefone de Contato: ')
            novo_servico_buffet["email_contato"] = input('E-mail de Contato: ')
            novo_servico_buffet["descricao_servico_buffet"] = input('Descrição do Serviço de Buffet: ')
            novo_servico_buffet["tipos_eventos_atendidos"] = input('Tipos de Eventos Atendidos (separados por vírgula): ').split(',')
            novo_servico_buffet["cardapios_oferecidos"] = input('Cardápios Oferecidos (separados por vírgula): ').split(',')
            novo_servico_buffet["capacidade_atendimento"] = input('Capacidade de Atendimento: ')
            novo_servico_buffet["horario_funcionamento"] = {}
            novo_servico_buffet["horario_funcionamento"]["segunda-feira"] = input('Horário de Funcionamento - Segunda-feira: ')
            novo_servico_buffet["horario_funcionamento"]["terca-feira"] = input('Horário de Funcionamento - Terça-feira: ')
            novo_servico_buffet["horario_funcionamento"]["quarta-feira"] = input('Horário de Funcionamento - Quarta-feira: ')
            novo_servico_buffet["horario_funcionamento"]["quinta-feira"] = input('Horário de Funcionamento - Quinta-feira: ')
            novo_servico_buffet["horario_funcionamento"]["sexta-feira"] = input('Horário de Funcionamento - Sexta-feira: ')
            novo_servico_buffet["horario_funcionamento"]["sabado"] = input('Horário de Funcionamento - Sábado: ')
            novo_servico_buffet["horario_funcionamento"]["domingo"] = input('Horário de Funcionamento - Domingo: ')
            novo_servico_buffet["faixa_preco_por_pessoa"] = input('Faixa de Preço por Pessoa: ')
            novo_servico_buffet["redes_sociais_website"] = {}
            novo_servico_buffet["redes_sociais_website"]["instagram"] = input('Instagram: ')
            novo_servico_buffet["redes_sociais_website"]["website"] = input('Website: ')
            buffet['buffet'].append(novo_servico_buffet)
            salvar_servicos_buffet(buffet)
            voltamenu()

        case 4:
            limpar()
            artista = carregar_banda_artista()
            banda_artista = {}
            banda_artista["nome_banda_artista"] = input('Nome da Banda/Artista: ')
            banda_artista["genero_musical"] = input('Gênero Musical: ')
            banda_artista["localizacao"] = {}
            banda_artista["localizacao"]["cidade"] = input('Localização (Cidade): ')
            banda_artista["localizacao"]["estado_provincia"] = input('Localização (Estado/Província): ')
            banda_artista["telefone_contato"] = input('Telefone de Contato: ')
            banda_artista["email_contato"] = input('E-mail de Contato: ')
            banda_artista["descricao_banda_artista"] = input('Descrição da Banda/Artista: ')
            banda_artista["repertorio"] = input('Repertório (principais músicas ou estilos tocados): ')
            banda_artista["disponibilidade_agendamento"] = {}
            banda_artista["disponibilidade_agendamento"]["dias_semana"] = input('Dias da Semana (separados por vírgula): ').split(',')
            banda_artista["disponibilidade_agendamento"]["horarios_disponiveis"] = input('Horários Disponíveis: ')
            banda_artista["faixa_preco_apresentacao"] = {}
            banda_artista["faixa_preco_apresentacao"]["preco_base"] = input('Preço base por Apresentação: ')
            banda_artista["faixa_preco_apresentacao"]["custos_adicionais"] = input('Custos adicionais (se aplicável): ')
            banda_artista["links_performance"] = input('Links de Performance (separados por vírgula): ').split(',')
            banda_artista["website"] = input('Website (se aplicável): ')
            banda_artista["instagram"] = input('Instagram (se aplicável): ')
            artista['artista'].append(banda_artista)
            salvar_banda_artista(banda_artista)
            voltamenu()

        case 5:
            limpar()
            seguranca=carregar_servicos_seguranca()
            servicos_seguranca = {}
            servicos_seguranca["nome_servico_seguranca"] = input('Nome do Serviço de Segurança: ')
            servicos_seguranca["localizacao"]["cidade"] = input('Localização (Cidade): ')
            servicos_seguranca["localizacao"]["estado_provincia"] = input('Localização (Estado/Província): ')
            servicos_seguranca["telefone_contato"] = input('Telefone de Contato: ')
            servicos_seguranca["email_contato"] = input('E-mail de Contato: ')
            servicos_seguranca["especialidades_seguranca"] = input('Especialidades de Segurança: ')
            servicos_seguranca["equipe_seguranca"]["numero_funcionarios"] = int(input('Equipe de Segurança (número de funcionários): '))
            servicos_seguranca["equipe_seguranca"]["experiencia"] = input('Equipe de Segurança (experiência): ')
            servicos_seguranca["licencas_certificacoes"] = input('Licenças e Certificações (se aplicável): ')
            servicos_seguranca["disponibilidade_servico"]["horarios_disponiveis"] = input('Horários Disponíveis: ')
            servicos_seguranca["disponibilidade_servico"]["dias_semana"] = input('Dias da Semana (separados por vírgula): ').split(',')
            servicos_seguranca["faixa_preco_servico"]["preco_base"] = input('Preço base por Serviço: ')
            servicos_seguranca["faixa_preco_servico"]["custos_adicionais"] = input('Custos adicionais (se aplicável): ')
            seguranca['seguranca'].append(servicos_seguranca)
            salvar_servicos_seguranca(servicos_seguranca)
            voltamenu()

        case 6:
            limpar()
            fotografia = carregar_servicos_fotografia()
            servicos_fotografia = {}
            servicos_fotografia["nome_servico_fotografia"] = input('Nome do Serviço de Fotografia: ')
            servicos_fotografia["localizacao"]["cidade"] = input('Localização (Cidade): ')
            servicos_fotografia["localizacao"]["estado_provincia"] = input('Localização (Estado/Província): ')
            servicos_fotografia["telefone_contato"] = input('Telefone de Contato: ')
            servicos_fotografia["email_contato"] = input('E-mail de Contato: ')
            servicos_fotografia["especialidade_fotografica"] = input('Especialidade Fotográfica: ')
            servicos_fotografia["descricao_servico"] = input('Descrição do Serviço de Fotografia: ')
            servicos_fotografia["portfolio"] = input('Portfólio: ')
            servicos_fotografia["disponibilidade_agendamento"]["horarios_disponiveis"] = input('Horários Disponíveis: ')
            servicos_fotografia["disponibilidade_agendamento"]["dias_semana"] = input('Dias da Semana (separados por vírgula): ').split(',')
            servicos_fotografia["faixa_preco_servico"]["preco_base"] = input('Preço base por Serviço: ')
            servicos_fotografia["faixa_preco_servico"]["custos_adicionais"] = input('Custos adicionais (se aplicável): ')
            servicos_fotografia["redes_sociais_website"]["instagram"] = input('Instagram: ')
            servicos_fotografia["redes_sociais_website"]["website"] = input('Website (se aplicável): ')
            fotografia['fotografia'].append(servicos_fotografia)
            salvar_servicos_fotografia(servicos_fotografia)
            voltamenu()

        case 7:
            limpar()
            print("Escolha o serviço que deseja atualizar:")
            print("1 - Local para evento")
            print("2 - Serviço de Bebidas")
            print("3 - Serviço de Buffet")
            print("4 - Bandas e Artistas")
            print("5 - Serviço de Segurança")
            print("6 - Serviço de Fotografia")
            servico_escolhido = int(input("Digite o número correspondente ao serviço: "))
            
            if servico_escolhido==1:
                limpar()
                arquivo_json = 'local_evento.json'
                estrutura = 'locais'  
                valor_antigo = input("Digite o valor antigo que deseja substituir: ")
                novo_valor = input("Digite o novo valor: ")
                atualizar_valor_json(arquivo_json, estrutura, valor_antigo, novo_valor)
                voltamenu()

            if servico_escolhido==2:
                limpar()
                arquivo_json = 'servicos_bebidas.json'
                estrutura = 'bebidas'
                valor_antigo = input("Digite o valor antigo que deseja substituir: ")
                novo_valor = input("Digite o novo valor: ")
                atualizar_valor_json(arquivo_json, estrutura, valor_antigo, novo_valor)
                voltamenu()

            if servico_escolhido==3:
                limpar()
                arquivo_json = 'servicos_buffet'
                estrutura = 'buffet'
                valor_antigo = input("Digite o valor antigo que deseja substituir: ")
                novo_valor = input("Digite o novo valor: ")
                atualizar_valor_json(arquivo_json, estrutura, valor_antigo, novo_valor)
                voltamenu()

            if servico_escolhido==4:
                limpar()
                arquivo_json = 'artista.json'
                estrutura = 'artista'
                valor_antigo = input("Digite o valor antigo que deseja substituir: ")
                novo_valor = input("Digite o novo valor: ")
                atualizar_valor_json(arquivo_json, estrutura, valor_antigo, novo_valor)
                voltamenu()

            if servico_escolhido==5:
                limpar()
                arquivo_json = 'seg.json'
                estrutura = 'seguranca'
                valor_antigo = input("Digite o valor antigo que deseja substituir: ")
                novo_valor = input("Digite o novo valor: ")
                atualizar_valor_json(arquivo_json, estrutura, valor_antigo, novo_valor)
                voltamenu()

            if servico_escolhido==6:
                limpar()
                arquivo_json = 'fotografia.json'
                estrutura = 'fotografia'
                valor_antigo = input("Digite o valor antigo que deseja substituir: ")
                novo_valor = input("Digite o novo valor: ")
                atualizar_valor_json(arquivo_json, estrutura, valor_antigo, novo_valor)
                voltamenu()

            else:
                print('Código Inválido!')
                voltamenu()
           
        case 8:

            limpar()
            print("Escolha o serviço que deseja atualizar:")
            print("1 - Local para evento")
            print("2 - Serviço de Bebidas")
            print("3 - Serviço de Buffet")
            print("4 - Bandas e Artistas")
            print("5 - Serviço de Segurança")
            print("6 - Serviço de Fotografia")
            servico_escolhido = int(input("Insira o código do serviço onde será realizada a exclusão: "))

            if servico_escolhido == 1:
                print ('Você deseja: ')
                print ('1- Excluir apenas um item específico')
                print ('2- Excluir um serviço específico')
                print ('3- Excluir todos os dados já registrados para Locais')
                opcao = int(input('Insira o código desejado: '))

                if opcao ==1:
                    arquivo_json = 'local_evento.json'
                    estrutura = 'locais' 
                    valor = input("Digite o valor que deseja excluir: ")
                    excluir_valor_json(arquivo_json, estrutura, valor)
                    voltamenu()
                
                if opcao ==2:
                    arquivo_json = 'local_evento.json'
                    estrutura = 'locais'  
                    print ('Índice(0-N° de Serviços adicionados): ')
                    indice = int(input("Digite o índice do elemento que deseja excluir: "))
                    excluir_elemento_json(arquivo_json, estrutura, indice)
                    voltamenu()
                
                if opcao ==3:
                    arquivo_json = 'local_evento.json'
                    estrutura = 'locais' 
                    limpar_array_json(arquivo_json, estrutura)
                    print(f"Todas as informações de '{estrutura}' foram limpas no arquivo.")
                    voltamenu()

            if servico_escolhido == 2:
                print ('Você deseja: ')
                print ('1- Excluir apenas um item específico')
                print ('2- Excluir um serviço específico')
                print ('3- Excluir todos os dados já registrados para Bebidas')
                opcao = int(input('Insira o código desejado: '))

                if opcao ==1:
                    arquivo_json = 'servicos_bebidas.json'
                    estrutura = 'bebidas' 
                    valor = input("Digite o valor que deseja excluir: ")
                    excluir_valor_json(arquivo_json, estrutura, valor)
                    voltamenu()
                
                if opcao ==2:
                    arquivo_json = 'servicos_bebidas.json'
                    estrutura = 'bebidas' 
                    print ('Índice(0-N° de Serviços adicionados): ')
                    indice = int(input("Digite o índice do elemento que deseja excluir: "))
                    excluir_elemento_json(arquivo_json, estrutura, indice)
                    voltamenu()
                
                if opcao ==3:
                    arquivo_json = 'servicos_bebidas.json'
                    estrutura = 'bebidas' 
                    limpar_array_json(arquivo_json, estrutura)
                    print(f"Todas as informações de '{estrutura}' foram limpas no arquivo.")
                    voltamenu()

            if servico_escolhido == 3:
                print ('Você deseja: ')
                print ('1- Excluir apenas um item específico')
                print ('2- Excluir um serviço específico')
                print ('3- Excluir todos os dados já registrados para Buffet')
                opcao = int(input('Insira o código desejado: '))

                if opcao ==1:
                    arquivo_json = 'servicos_buffet.json'
                    estrutura = 'buffet' 
                    valor = input("Digite o valor que deseja excluir: ")
                    excluir_valor_json(arquivo_json, estrutura, valor)
                    voltamenu()
                
                if opcao ==2:
                    arquivo_json = 'servicos_buffet.json'
                    estrutura = 'buffet' 
                    print ('Índice(0-N° de Serviços adicionados): ')
                    indice = int(input("Digite o índice do elemento que deseja excluir: "))
                    excluir_elemento_json(arquivo_json, estrutura, indice)
                    voltamenu()
                
                if opcao ==3:
                    arquivo_json = 'servicos_buffet.json'
                    estrutura = 'buffet' 
                    limpar_array_json(arquivo_json, estrutura)
                    print(f"Todas as informações de '{estrutura}' foram limpas no arquivo.")
                    voltamenu()

            if servico_escolhido == 4:
                print ('Você deseja: ')
                print ('1- Excluir apenas um item específico')
                print ('2- Excluir um serviço específico')
                print ('3- Excluir todos os dados já registrados para Artistas')
                opcao = int(input('Insira o código desejado: '))

                if opcao ==1:
                    arquivo_json = 'artista.json'
                    estrutura = 'artista' 
                    valor = input("Digite o valor que deseja excluir: ")
                    excluir_valor_json(arquivo_json, estrutura, valor)
                    voltamenu()
                
                if opcao ==2:
                    arquivo_json = 'artista.json'
                    estrutura = 'artista' 
                    print ('Índice(0-N° de Serviços adicionados): ')
                    indice = int(input("Digite o índice do elemento que deseja excluir: "))
                    excluir_elemento_json(arquivo_json, estrutura, indice)
                    voltamenu()
                
                if opcao ==3:
                    arquivo_json = 'artista.json'
                    estrutura = 'artista' 
                    limpar_array_json(arquivo_json, estrutura)
                    print(f"Todas as informações de '{estrutura}' foram limpas no arquivo.")
                    voltamenu()

            if servico_escolhido == 5:
                print ('Você deseja: ')
                print ('1- Excluir apenas um item específico')
                print ('2- Excluir um serviço específico')
                print ('3- Excluir todos os dados já registrados para Segurança')
                opcao = int(input('Insira o código desejado: '))

                if opcao ==1:
                    arquivo_json = 'seg.json'
                    estrutura = 'seguranca' 
                    valor = input("Digite o valor que deseja excluir: ")
                    excluir_valor_json(arquivo_json, estrutura, valor)
                    voltamenu()
                
                if opcao ==2:
                    arquivo_json = 'seg.json'
                    estrutura = 'seguranca' 
                    print ('Índice(0-N° de Serviços adicionados): ')
                    indice = int(input("Digite o índice do elemento que deseja excluir: "))
                    excluir_elemento_json(arquivo_json, estrutura, indice)
                    voltamenu()
                
                if opcao ==3:
                    arquivo_json = 'seg.json'
                    estrutura = 'seguranca' 
                    limpar_array_json(arquivo_json, estrutura)
                    print(f"Todas as informações de Segurança foram limpas no arquivo.")
                    voltamenu()

            if servico_escolhido == 6:
                print ('Você deseja: ')
                print ('1- Excluir apenas um item específico')
                print ('2- Excluir um serviço específico')
                print ('3- Excluir todos os dados já registrados para Fotografia')
                opcao = int(input('Insira o código desejado: '))

                if opcao ==1:
                    arquivo_json = 'fotografia.json'
                    estrutura = 'fotografia' 
                    valor = input("Digite o valor que deseja excluir: ")
                    excluir_valor_json(arquivo_json, estrutura, valor)
                    voltamenu()
                
                if opcao ==2:
                    arquivo_json = 'fotografia.json'
                    estrutura = 'fotografia' 
                    print ('Índice(0-N° de Serviços adicionados): ')
                    indice = int(input("Digite o índice do elemento que deseja excluir: "))
                    excluir_elemento_json(arquivo_json, estrutura, indice)
                    voltamenu()
                
                if opcao ==3:
                    arquivo_json = 'fotografia.json'
                    estrutura = 'fotografia' 
                    limpar_array_json(arquivo_json, estrutura)
                    print(f"Todas as informações de fotografia foram limpas no arquivo.")
                    voltamenu()

        case 9:
             
            limpar()
            print("Escolha o serviço que deseja atualizar:")
            print("1 - Local para evento")
            print("2 - Serviço de Bebidas")
            print("3 - Serviço de Buffet")
            print("4 - Bandas e Artistas")
            print("5 - Serviço de Segurança")
            print("6 - Serviço de Fotografia")
            visualizar = int(input("Insira o código para visualizar serviço: "))

            if visualizar == 1:
                with open ('local_evento.json', 'r') as loc:
                    data = json.load(loc)
                print('Locais Cadastrados: ')
                for local in data['locais']:
                    print(f'\n Nome do Local: {local["nome_local"]}')
                    print(f'Endereço: {local["endereco"]}')
                    print(f'Cidade: {local["cidade"]}')
                    print(f'Estado: {local["estado_provincia"]}')
                    print(f'CEP: {local["cep"]}')
                    print(f'Telefone: {local["telefone_contato"]}')
                    print(f'E-mail: {local["email_contato"]}')
                    print(f'Tipo do Local: {local["tipo_local"]}')
                    print(f'Descrição do Local: {local["descricao_local"]}')
                    print('Horário de funcionamento: ')
                    print(f'Segunda-Feira: {local["horario_funcionamento"]["segunda-feira"]}')
                    print(f'Terça-Feira: {local["horario_funcionamento"]["terca-feira"]}')
                    print(f'Quarta-Feira: {local["horario_funcionamento"]["quarta-feira"]}')
                    print(f'Quinta-Feira: {local["horario_funcionamento"]["quinta-feira"]}')
                    print(f'Sexta-Feira: {local["horario_funcionamento"]["sexta-feira"]}')
                    print(f'Sábado: {local["horario_funcionamento"]["sabado"]}')
                    print(f'Domingo: {local["horario_funcionamento"]["domingo"]}')
                    
                    voltamenu()

            if visualizar == 2:
                with open ('servicos_bebidas.json', 'r') as loc:
                    data=json.load(loc)
                print('Serviços de bebida Cadastrados: ')
                for beb in data['bebidas']:
                    print(f'Nome do Local: {beb['nome_servico']}')
                    print(f'Endereço: {beb['endereco']}')
                    print(f'Cidade: {beb['cidade']}')
                    print(f'Estado: {beb['estado_provincia']}')
                    print(f'CEP: {beb['cep']}')
                    print(f'Telefone: {beb['telefone_contato']}')
                    print(f'E-mail: {beb['email_contato']}')
                    print(f'Tipo do serviço de bebidas: {beb['tipo_servico_bebidas']}')
                    print(f'Descrição do Local: {beb['descricao_servico']}')
                    print (f'Tipos de bebida oferecidas: {beb['tipo_bebidas_oferecidas']}')
                    print(f'Faixa de preço: {beb['faixa_preco']}')
                    print ('Redes Sociais:')
                    print (f'Instagram: {beb['redes_sociais_website']['instagram']}')
                    print (f'Website: {beb['redes_sociais_website']['website']}')
                    print (f'Open bar: {beb['open_bar']}')
                    print('Horário de funcionamento: ')
                    print(f'Segunda-Feira: {beb['horario_funcionamento']['segunda-feira']} ')
                    print(f'Terça-Feira: {beb['horario_funcionamento']['terca-feira']} ')
                    print(f'Quarta-Feira: {beb['horario_funcionamento']['quarta-feira']} ')
                    print(f'Quinta-Feira: {beb['horario_funcionamento']['quinta-feira']} ')
                    print(f'Sexta-Feira: {beb['horario_funcionamento']['sexta-feira']} ')
                    print(f'Sábado: {beb['horario_funcionamento']['sabado']} ')
                    print(f'Domingo: {beb['horario_funcionamento']['domingo']} ')
                    voltamenu()

            if visualizar == 3:
                with open ('servicos_buffet.json', 'r') as loc:
                    data=json.load(loc)
                print('Serviços de buffet Cadastrados: ')
                for buf in data['buffet']:
                    print(f'Nome do Local: {buf['nome_servico_buffet']}')
                    print(f'Endereço: {buf['endereco']}')
                    print(f'Cidade: {buf['cidade']}')
                    print(f'Estado: {buf['estado_provincia']}')
                    print(f'CEP: {buf['cep']}')
                    print(f'Telefone: {buf['telefone_contato']}')
                    print(f'E-mail: {buf['email_contato']}')
                    print(f'Tipo de eventos atendidos: {buf['tipo_eventos_atendidos']}')
                    print(f'Descrição do Local: {buf['descricao_servico_buffet']}')
                    print (f'Cardápios oferecidos: {buf['cardapios_oferecidos']}')
                    print(f'Faixa de preço por pessoa: {buf['faixa_preco_por_pessoa']}')
                    print (f'Capacidade de atendimento: {buf['capacidade_atendimento']}')
                    print ('Redes Sociais:')
                    print (f'Instagram: {buf['redes_sociais_website']['instagram']}')
                    print (f'Website: {buf['redes_sociais_website']['website']}')
                    print('Horário de funcionamento: ')
                    print(f'Segunda-Feira: {buf['horario_funcionamento']['segunda-feira']} ')
                    print(f'Terça-Feira: {buf['horario_funcionamento']['terca-feira']} ')
                    print(f'Quarta-Feira: {buf['horario_funcionamento']['quarta-feira']} ')
                    print(f'Quinta-Feira: {buf['horario_funcionamento']['quinta-feira']} ')
                    print(f'Sexta-Feira: {buf['horario_funcionamento']['sexta-feira']} ')
                    print(f'Sábado: {buf['horario_funcionamento']['sabado']} ')
                    print(f'Domingo: {buf['horario_funcionamento']['domingo']} ')
                    voltamenu()

            if visualizar == 4:
                with open ('artista.json', 'r') as loc:
                    data=json.load(loc)
                print('Artistas Cadastrados: ')
                for art in data['artista']:
                    print(f'Nome da Banda/Artista: {art['nome_banda_artista']}')
                    print(f'Gênero Musical: {art['genero_musical']}')
                    print(f'Cidade: {art['localizacao']['cidade']}')
                    print(f'Estado: {art['localizacao']['estado_provincia']}')
                    print(f'Telefone: {art['telefone_contato']}')
                    print(f'E-mail: {art['email_contato']}')
                    print(f'Descrição da Banda/Artista: {art['descricao_banda_artista']}')
                    print (f'Repertório: {art['repertorio']}')
                    print(f'Faixa de preço por apresentação: {art['faixa_preco_apresentacao']}')
                    print (f'Capacidade de atendimento: {art['capacidade_atendimento']}')
                    print (f'Links para performances: {art['links_performance']}')
                    print ('Redes Sociais:')
                    print (f'Instagram: {art['instagram']}')
                    print (f'Website: {art['website']}')
                    print('Disponibilidade de agendamento: ')
                    print(f'Dias da semana disponíveis: {art['disponibilidade_agendamento']['dias_semana']} ')
                    print(f'Horários disponíveis: {art['disponibilidade_agendamento']['horario_disponiveis']} ')
                    voltamenu()

            if visualizar == 5:
                with open ('seg.json', 'r') as loc:
                    data=json.load(loc)
                print('Serviços de segurança cadastrados: ')
                for seg in data['seguranca']:
                    print(f'Nome do serviço: {seg['nome_servico_seguranca']}')
                    print(f'Cidade: {seg['localizacao']['cidade']}')
                    print(f'Estado: {seg['localizacao']['estado_provincia']}')
                    print(f'Telefone: {seg['telefone_contato']}')
                    print(f'E-mail: {seg['email_contato']}')
                    print(f'Especialidade de segurança: {seg['especialidade_seguranca']}')
                    print ('Equipe de segurança: ')
                    print (f'Número de funcionários: {seg['equipe_seguranca']['numero_funcionarios']}')
                    print (f'Experiência: {seg['equipe_seguranca']['experiencia']}')
                    print (f'Licenças e Certificações: {seg['licencas_certificacoes']}')
                    print(f'Faixa de preço: ')
                    print(f'Preço Base: {seg['faixa_preco_servico']['preco_base']}')
                    print(f'Custos Adicionais: {seg['faixa_preco_servico']['custos_adicionais']}')
                    print('Disponibilidade de serviço: ')
                    print(f'Dias da semana disponíveis: {seg['disponibilidade_servico']['dias_semana']} ')
                    print(f'Horários disponíveis: {seg['disponibilidade_servico']['horario_disponiveis']} ')
                    voltamenu()

            if visualizar == 6:
                with open ('fotografia.json', 'r') as loc:
                    data=json.load(loc)
                print('Serviços de fotografia cadastrados: ')
                for fot in data['fotografia']:
                    print(f'Nome do serviço: {fot['nome_servico_fotografia']}')
                    print(f'Cidade: {fot['localizacao']['cidade']}')
                    print(f'Estado: {fot['localizacao']['estado_provincia']}')
                    print(f'Telefone: {fot['telefone_contato']}')
                    print(f'E-mail: {fot['email_contato']}')
                    print(f'Especialidade fotográfica: {fot['especialidade_fotografica']}')
                    print (f'Portfólio: {fot['portfolio']}')
                    print(f'Descrição do serviço: {fot['descricao_servico']}')
                    print(f'Faixa de preço: ')
                    print(f'Preço Base: {fot['faixa_preco_servico']['preco_base']}')
                    print(f'Custos Adicionais: {fot['faixa_preco_servico']['custos_adicionais']}')
                    print('Disponibilidade de serviço: ')
                    print(f'Dias da semana disponíveis: {fot['disponibilidade_servico']['dias_semana']} ')
                    print(f'Horários disponíveis: {fot['disponibilidade_servico']['horario_disponiveis']} ')
                    print ('Redes Sociais:')
                    print (f'Instagram: {fot['instagram']}')
                    print (f'Website: {fot['website']}')
                    voltamenu()
            
            else:
                print ('Código Inválido!')
                voltamenu()
        case 10:
            limpar()
            print('Encerrando...')
            sleep (5)
            exit()
        case _:
            limpar()
            print('Código inválido')
            voltamenu()


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        menuprincipal()
        escolhas()

if __name__ == '__main__':
    main()

