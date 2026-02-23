from modelo.usuario import Usuario

class Estudante(Usuario):
    def __init__(self, nome, email, senha, telefone, matricula, curso):
        super().__init__(nome, email, senha, telefone, matricula)
        self.__curso = curso

    def to_dict(self):
        dados = super().to_dict()
        dados.update({
            "curso": self.__curso
        })
        return dados

    def getCurso(self): 
        return self.__curso
        
    def setCurso(self, novo_curso):
        self.__curso = novo_curso
    
    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"Curso: {self.getCurso()}"
        )
