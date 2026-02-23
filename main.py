from controle.cadastro import Cadastro
from modelo.professor import Professor
from modelo.estudante import Estudante


def menu():
    print("\n===== SISTEMA DE CADASTRO =====")
    print("1 - Cadastrar Professor")
    print("2 - Cadastrar Aluno")
    print("3 - Listar Usuários")
    print("4 - Buscar Usuário")
    print("5 - Remover Usuário")
    print("0 - Sair")


def cadastrar_professor(cadastro):
    try:
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        matricula = input("Matrícula: ")

        senha = input("Senha: ")
        confirmar = input("Confirme a senha: ")

        if senha != confirmar:
            raise ValueError("As senhas não coincidem.")

        graduacao = input("Graduação: ")

        professor = Professor(
            nome, email, senha, telefone,
            matricula, graduacao
        )

        cadastro.inserir(professor)
        print("Professor cadastrado com sucesso!")

    except ValueError as e:
        print(f"Erro: {e}")


def cadastrar_aluno(cadastro):
    try:
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        matricula = input("Matrícula: ")

        senha = input("Senha: ")
        confirmar = input("Confirme a senha: ")

        if senha != confirmar:
            raise ValueError("As senhas não coincidem.")

        curso = input("Curso: ")

        aluno = Estudante(
            nome, email, senha, telefone,
            matricula, curso
        )

        cadastro.inserir(aluno)
        print("Aluno cadastrado com sucesso!")

    except ValueError as e:
        print(f"Erro: {e}")


def listar_usuarios(cadastro):
    usuarios = cadastro.listar()

    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for usuario in usuarios:
        print("----------------------")
        print(usuario)


def buscar_usuario(cadastro):
    try:
        matricula = input("Digite a matrícula: ")
        usuario = cadastro.buscar(matricula)
        print(usuario)

    except ValueError as e:
        print(f"Erro: {e}")


def remover_usuario(cadastro):
    try:
        matricula = input("Digite a matrícula: ")
        cadastro.remover(matricula)
        print("Usuário removido com sucesso!")

    except ValueError as e:
        print(f"Erro: {e}")


def main():
    cadastro = Cadastro("dados.json")

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_professor(cadastro)

        elif opcao == "2":
            cadastrar_aluno(cadastro)

        elif opcao == "3":
            listar_usuarios(cadastro)

        elif opcao == "4":
            buscar_usuario(cadastro)

        elif opcao == "5":
            remover_usuario(cadastro)

        elif opcao == "0":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()