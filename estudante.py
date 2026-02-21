from Usuario import Usuario

class Estudante(Usuario):
    def __init__(self, nome, email, senha, curso, matricula):
        # 1. Envia os dados básicos para a classe mãe (Usuario) validar e salvar.
        # O tipo de perfil é fixado como "Estudante".
        super().__init__(nome, email, senha, "Estudante")
        
        # 2. Inicializa os atributos específicos com valores padrão seguros
        self.__curso = "Não definido"
        self.__matricula = "0000"
        
        # 3. Usa os setters para aplicar os valores digitados passando pelas regras
        self.setCurso(curso)
        self.setMatricula(matricula)

    # ==============================
    # GETTERS (Leitura)
    # ==============================
    def getCurso(self): 
        return self.__curso
        
    def getMatricula(self): 
        return self.__matricula

    # ==============================
    # SETTERS (Modificação e Validação)
    # ==============================
    def setCurso(self, novo_curso):
        # O curso deve ter mais de 2 caracteres e não ser apenas espaços
        if len(novo_curso.strip()) > 2:
            self.__curso = novo_curso.strip()
        else:
            print("Erro: O nome do curso deve ser válido.")

    def setMatricula(self, nova_matricula):
        # A matrícula deve ter pelo menos 4 caracteres e não conter espaços
        if len(nova_matricula.strip()) >= 4 and " " not in nova_matricula:
            self.__matricula = nova_matricula.strip()
        else:
            print("Erro: A matrícula deve ter pelo menos 4 caracteres e sem espaços.")

    # ==============================
    # IMPRESSÃO
    # ==============================
    def imprimeInfo(self):
        super().imprimeInfo() # Chama a impressão do Pai (Nome, Email, Perfil)
        print(f"Curso: {self.getCurso()}")
        print(f"Matrícula: {self.getMatricula()}")
        print("-" * 24)
