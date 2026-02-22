from usuario import Usuario

class Estudante(Usuario):
    def __init__(self, nome, email, senha, matricula, curso):
        super().__init__(nome, email, senha, matricula)
        self.__curso = curso

    def getCurso(self): 
        return self.__curso
        
    def setCurso(self, novo_curso):
        self.__curso = novo_curso