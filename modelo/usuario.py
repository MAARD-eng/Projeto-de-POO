import re


class Usuario:

    def __init__(self, nome, email, senha, telefone, matricula=None):

        self.setNome(nome)
        self.setEmail(email)
        self.setSenha(senha)
        self.setTelefone(telefone)

        # matrícula pode ser definida depois pelo Cadastro
        self.__matricula = matricula


    # =========================
    # VALIDAÇÕES
    # =========================

    def validar_email(self, email):

        padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(padrao, email):
            raise ValueError("Email inválido")


    def validar_senha(self, senha):

        if len(senha) < 6:
            raise ValueError("Senha deve ter pelo menos 6 caracteres")


    def validar_telefone(self, telefone):

        padrao = r'^\d{8,15}$'

        if telefone and not re.match(padrao, telefone):
            raise ValueError("Telefone deve conter apenas números (8 a 15 dígitos)")


    # =========================
    # GETTERS
    # =========================

    def getNome(self):
        return self.__nome

    def getEmail(self):
        return self.__email

    def getSenha(self):
        return self.__senha

    def getTelefone(self):
        return self.__telefone

    def getMatricula(self):
        return self.__matricula


    # =========================
    # SETTERS COM VALIDAÇÃO
    # =========================

    def setNome(self, nome):

        if not nome.strip():
            raise ValueError("Nome não pode ser vazio")

        self.__nome = nome


    def setEmail(self, email):

        self.validar_email(email)

        self.__email = email


    def setSenha(self, senha):

        self.validar_senha(senha)

        self.__senha = senha


    def setTelefone(self, telefone):

        self.validar_telefone(telefone)

        self.__telefone = telefone


    def setMatricula(self, matricula):

        self.__matricula = matricula


    # =========================
    # SERIALIZAÇÃO
    # =========================

    def to_dict(self):

        return {

            "tipo": self.__class__.__name__,
            "nome": self.__nome,
            "email": self.__email,
            "senha": self.__senha,
            "telefone": self.__telefone,
            "matricula": self.__matricula

        }


    # =========================
    # STRING
    # =========================

    def __str__(self):

        return (

            f"Matrícula: {self.__matricula}\n"
            f"Nome: {self.__nome}\n"
            f"Email: {self.__email}\n"
            f"Telefone: {self.__telefone}\n"

        )
