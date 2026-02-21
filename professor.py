from usuario import Usuario

class Professor(Usuario):
    def __init__(self, nome, email, senha, departamento, titulacao):
        # 1. Envia os dados básicos para a classe mãe (Usuario).
        # O tipo de perfil é fixado como "Professor".
        super().__init__(nome, email, senha, "Professor")
        
        # 2. Inicializa os atributos específicos com valores padrão
        self.__departamento = "Não definido"
        self.__titulacao = "Não definida"
        
        # 3. Usa os setters para validar os dados específicos
        self.setDepartamento(departamento)
        self.setTitulacao(titulacao)

    # ==============================
    # GETTERS (Leitura)
    # ==============================
    def getDepartamento(self): 
        return self.__departamento
        
    def getTitulacao(self): 
        return self.__titulacao

    # ==============================
    # SETTERS (Modificação e Validação)
    # ==============================
    def setDepartamento(self, novo_departamento):
        # O departamento deve ter mais de 2 caracteres
        if len(novo_departamento.strip()) > 2:
            self.__departamento = novo_departamento.strip()
        else:
            print("Erro: Departamento inválido.")

    def setTitulacao(self, nova_titulacao):
        # Só aceita as titulações predefinidas pelo sistema
        titulacoes_validas = ["Especialista", "Mestre", "Doutor", "Pós-Doutor"]
        
        if nova_titulacao in titulacoes_validas:
            self.__titulacao = nova_titulacao
        else:
            print(f"Erro: Titulação inválida. Escolha entre: {', '.join(titulacoes_validas)}")

    # ==============================
    # IMPRESSÃO
    # ==============================
    def imprimeInfo(self):
        super().imprimeInfo() # Imprime os dados gerais do Usuário
        print(f"Departamento: {self.getDepartamento()}")
        print(f"Titulação: {self.getTitulacao()}")
        print("-" * 24)
