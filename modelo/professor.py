from modelo.usuario import Usuario

class Professor(Usuario):
    def __init__(self, nome, email, senha, telefone, matricula, graduacao):
        super().__init__(nome, email, senha, telefone, matricula)
        self.__graduacao = graduacao

    def to_dict(self):
        dados = super().to_dict()
        dados.update({
            "titulacao": self.__graduacao
        })
        return dados

    def getGraduacao(self): 
        return self.__graduacao
    
    def setGraduacao(self, nova_graduacao):
        self.__graduacao = nova_graduacao

    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"Graduação: {self.getGraduacao()}"
        )