import re

class Usuario:
    def __init__(self, nome, email, senha, telefone, matricula):
        self.setNome(nome)
        self.setEmail(email)
        self.setSenha(senha)
        self.setTelefone(telefone)
        self.setMatricula(matricula)
    
    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "nome": self.__nome,
            "email": self.__email,
            "senha": self.__senha,
            "telefone": self.__telefone,
            "matricula": self.__matricula
        }

    # GETTERS

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


    # SETTERS COM VALIDAÇÃO

    def setNome(self, novo_nome):
        if len(novo_nome.strip()) < 3:
            raise ValueError("Nome deve ter pelo menos 3 caracteres")
        self.__nome = novo_nome
    

    def setEmail(self, novo_email):

        padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(padrao, novo_email):
            raise ValueError("Email inválido")

        self.__email = novo_email
    

    def setSenha(self, nova_senha):

        if len(nova_senha) < 6:
            raise ValueError("Senha deve ter pelo menos 6 caracteres")

        if not any(char.isdigit() for char in nova_senha):
            raise ValueError("Senha deve conter pelo menos 1 número")

        self.__senha = nova_senha


    def setTelefone(self, novo_telefone):

        padrao = r"^\d{10,11}$"

        if not re.match(padrao, novo_telefone):
            raise ValueError("Telefone deve ter 10 ou 11 dígitos")

        self.__telefone = novo_telefone
    

    def setMatricula(self, nova_matricula):

        if len(str(nova_matricula)) < 3:
            raise ValueError("Matricula inválida")

        self.__matricula = nova_matricula
    

    def __str__(self):
        return (
            f"Matricula: {self.getMatricula()}\n"
            f"Nome: {self.getNome()}\n"
            f"Email: {self.getEmail()}\n"
            f"Telefone: {self.getTelefone()}\n"
        )
