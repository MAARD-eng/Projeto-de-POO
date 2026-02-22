from modelo.usuario import Usuario

class Professor(Usuario):
    def __init__(self, nome, email, senha, telefone, matricula, graduacao):
        super().__init__(nome, email, senha, telefone, matricula)
        self.__graduacao = graduacao

    def getGraduacao(self): 
        return self.__graduacao
    
    def setGraduacao(self, nova_graduacao):
        self.__graduacao = nova_graduacao
