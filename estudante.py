from Usuario import Usuario

class Estudante(Usuario):
    def __init__(self, nome, email, senha, curso, matricula):
        super().__init__(nome, email, senha, "Estudante")
        # Chama os setters para garantir a validação logo na criação
        self.setCurso(curso)
        self.setMatricula(matricula)

    # ==============================
    # GETTERS
    # ==============================
    def getCurso(self): 
        return self.__curso
        
    def getMatricula(self): 
        return self.__matricula

    # ==============================
    # SETTERS (Com validações)
    # ==============================
    def setCurso(self, novo_curso):
        # Garante que o nome do curso não seja apenas espaços em branco
        if len(novo_curso.strip()) > 2:
            self.__curso = novo_curso.strip()
        else:
            print("Erro: O nome do curso deve ser válido.")
            self.__curso = "Não definido" # Valor padrão de segurança

    def setMatricula(self, nova_matricula):
        # Exemplo de regra: A matrícula deve ter pelo menos 4 caracteres e não ter espaços
        if len(nova_matricula.strip()) >= 4 and " " not in nova_matricula:
            self.__matricula = nova_matricula.strip()
        else:
            print("Erro: A matrícula deve ter pelo menos 4 caracteres e sem espaços.")
            self.__matricula = "0000"

    # ==============================
    # IMPRESSÃO
    # ==============================
    def imprimeInfo(self):
        super().imprimeInfo() # Chama o print do pai (Nome, Email, Perfil)
        print(f"Curso: {self.getCurso()}")
        print(f"Matrícula: {self.getMatricula()}")
        print("-" * 24)
