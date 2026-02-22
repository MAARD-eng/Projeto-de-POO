class Usuario:
    def __init__(self, nome, email, senha, telefone, matricula):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__matricula = matricula
        self.__telefone = telefone
    
    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "nome": self.__nome,
            "email": self.__email,
            "senha": self.__senha,
            "telefone": self.__telefone,
            "matricula": self.__matricula
        }

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
    
    def setNome(self, novo_nome):
        self.__nome = novo_nome
    
    def setEmail(self, novo_email):
        self.__email = novo_email
    
    def setSenha(self, nova_senha):
        self.__senha = nova_senha

    def setTelefone(self, novo_telefone):
        self.__telefone = novo_telefone
    
    def setMatricula(self, nova_matricula):
        self.__matricula = nova_matricula
    
    def __str__(self):
        return (
            f"Matricula: {self.getMatricula}\n"
            f"Nome: {self.getNome}\n"
            f"Email: {self.getEmail}\n"
            f"Telefone: {self.getTelefone}\n"
        )