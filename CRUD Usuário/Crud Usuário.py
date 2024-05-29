class Usuario:
    def _init_(self, nome: str, telefone: str, email: str):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def _str_(self) -> str:
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"

class SistemaUsuarios:
    def _init_(self):
        self.usuarios: list[Usuario] = []

    def adicionar_usuario(self, usuario: Usuario) -> None:
        self.usuarios.append(usuario)
        print("Usuário adicionado com sucesso.")

    def listar_usuarios(self) -> None:
        if self.usuarios:
            print("Lista de Usuários:")
            for i, usuario in enumerate(self.usuarios, start=1):
                print(f"{i}. {usuario}")
        else:
            print("Não há usuários no sistema.")

    def atualizar_usuario(self, nome: str, novo_nome: str = None, telefone: str = None, email: str = None) -> None:
        for usuario in self.usuarios:
            if usuario.nome == nome:
                if novo_nome:
                    usuario.nome = novo_nome
                if telefone:
                    usuario.telefone = telefone
                if email:
                    usuario.email = email
                print("Usuário atualizado com sucesso.")
                return
        print("Usuário não encontrado.")

    def excluir_usuario(self, nome: str) -> None:
        for usuario in self.usuarios:
            if usuario.nome == nome:
                self.usuarios.remove(usuario)
                print("Usuário excluído com sucesso.")
                return
        print("Usuário não encontrado.")

def menu() -> None:
    print("\n=== MENU ===")
    print("1. Adicionar Usuário")
    print("2. Listar Usuários")
    print("3. Atualizar Usuário")
    print("4. Excluir Usuário")
    print("5. Sair")

def obter_input_usuario() -> Usuario:
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    return Usuario(nome, telefone, email)

def obter_input_atualizacao() -> dict:
    novo_nome = input("Novo Nome (pressione Enter para manter o atual): ")
    telefone = input("Novo Telefone (pressione Enter para manter o atual): ")
    email = input("Novo Email (pressione Enter para manter o atual): ")
    return {"novo_nome": novo_nome, "telefone": telefone, "email": email}

def main() -> None:
    sistema = SistemaUsuarios()
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            usuario = obter_input_usuario()
            sistema.adicionar_usuario(usuario)
        elif opcao == '2':
            sistema.listar_usuarios()
        elif opcao == '3':
            nome = input("Nome do Usuário a ser atualizado: ")
            atualizacoes = obter_input_atualizacao()
            sistema.atualizar_usuario(
                nome, 
                novo_nome=atualizacoes["novo_nome"] or None, 
                telefone=atualizacoes["telefone"] or None, 
                email=atualizacoes["email"] or None
            )
        elif opcao == '4':
            nome = input("Nome do Usuário a ser excluído: ")
            sistema.excluir_usuario(nome)
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__== "_main_": main()