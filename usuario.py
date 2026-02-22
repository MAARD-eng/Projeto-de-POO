class Usuario:
    def __init__(self, nome, email, senha, matricula):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__matricula = matricula 

    def getNome(self):
        return self.__nome

    def getEmail(self):
        return self.__email
        
    def getSenha(self):
        return self.__senha

    def getMatricula(self):
        return self.__matricula


    def setNome(self, novo_nome):
        self.__nome = novo_nome
    
    def setEmail(self, novo_email):
        self.__email = novo_email
    
    def setSenha(self, nova_senha):
        self.__senha = nova_senha

    def setMatricula(self, nova_matricula):
        self.__matricula = nova_matricula

        
