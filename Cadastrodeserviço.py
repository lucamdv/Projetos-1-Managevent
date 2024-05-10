import os

opcao = []
def limpar ():
     os.system('cls')

def menuprincipal ():
    limpar()
    print('Menu de Eventos')
    print ('1- Local para evento')
    print ('2- Serviço de Bebidas')
    print ('3- Serviço de Buffet')
    print ('4- Bandas e Artistas')
    print ('5- Segurança (Bombeiros, Paramédicos, Vigilância)')
    print ('6- Fotografia')
    print ('7- Atualizar meu serviço')
    print ('8- Excluir meu serviço')
    print ('9- Sair')

    global codigo
    codigo =  int(input('\n Digite o código do que deseja: '))

def voltamenu():
    input('Digite qualquer tecla para voltar ao menu principal')
    main()
  
def escolhas():
    
    match(codigo):
        case 1:
            global local 
            limpar()
            local = input('Insira o nome do seu local: ')
            opcao.append(local)
            voltamenu()
        case 2:
            global bebida
            limpar()
            bebida = input('Insira o nome do seu serviço de bebidas: ')
            opcao.append(bebida)
            voltamenu()
        case 3:
            global buffet
            limpar()
            buffet = input('Insira o nome do seu serviço de buffet: ')
            opcao.append(buffet)
            voltamenu()
        case 4:
            global bandas
            limpar()
            bandas = input('Insira o nome da banda/artista: ')
            opcao.append(bandas)
            voltamenu()
        case 5:
            global segurança
            limpar()
            segurança = input('Insira o nome do seu serviço de segurança: ')
            opcao.append(segurança)
            voltamenu()
        case 6:
            global fotografia
            limpar()
            fotografia = input('Insira o nome do seu serviço de fotografia: ')
            opcao.append(fotografia)
            voltamenu()
        case 7: 
            global atualizar, remover
            limpar()
            remover = opcao.remove(input('Digite o nome do serviço a ser removido: '))
            atualizar = input('Digite o novo valor do serviço desejado: ')
            opcao.append(atualizar)
            voltamenu()
        case 8:
            limpar()
            remover = opcao.remove(input('Digite o nome do serviço a ser removido: '))
            voltamenu()
        case 9:
            limpar()
            print ('Foram adicionados os serviços: {}'.format(opcao))
            print ('Programa finalizado! Seus serviços foram adicionados com sucesso!')
        case _:
            limpar()
            print('Código inválido')
            voltamenu()

def main ():
    os.system ('cls')
    menuprincipal()
    escolhas()

if __name__ == '__main__':
    main()
