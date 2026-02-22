from usuario import Usuario

class Professor(Usuario):
    def __init__(self, nome, email, senha, matricula, departamento):
        super().__init__(nome, email, senha, matricula)
        self.__departamento = departamento 

    def getDepartamento(self): 
        return self.__departamento
    
    def setDepartamento(self, novo_departamento):
        self.__departamento = novo_departamento
