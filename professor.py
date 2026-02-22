from usuario import Usuario

class Professor(Usuario):
    def __init__(self, nome, email, senha, matricula, graduacao):
        super().__init__(nome, email, senha, matricula)
        self.__graduacao = graduacao

    def getGraduacao(self): 
        return self.__graduacao
    
    def setGraduacao(self, nova_graduacao):
        self.__graduacao = nova_graduacao
