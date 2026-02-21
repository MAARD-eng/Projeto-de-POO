class Usuario:
    def __init__(self, nome, email, senha, tipo_perfil):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__tipo_perfil = tipo_perfil 

    # ==============================
    # GETTERS (Métodos de Leitura)
    # ==============================
    def getNome(self):
        return self.__nome

    def getEmail(self):
        return self.__email
        
    def getSenha(self):
        return self.__senha

    def getTipoPerfil(self):
        return self.__tipo_perfil

    # ==============================
    # SETTERS (Métodos de Modificação e Validação)
    # ==============================
    def setNome(self, novo_nome):
        # Nome precisa ter pelo menos 3 letras e não ser apenas espaços
        if len(novo_nome.strip()) > 2:
            self.__nome = novo_nome.strip()
        else:
            print("Erro: O nome deve ter mais de 2 caracteres válidos.")

    def setEmail(self, novo_email):
        # Validação mais rigorosa: Exige '@', '.' e proíbe espaços em branco
        if "@" in novo_email and "." in novo_email and " " not in novo_email:
            self.__email = novo_email.lower() # Opcional: já guarda o email em minúsculas
        else:
            print("Erro: E-mail inválido. Deve conter '@', '.' e não ter espaços.")

    def setSenha(self, nova_senha):
        # Exige entre 6 e 15 caracteres e impede senhas com espaços
        if 6 <= len(nova_senha) <= 15 and " " not in nova_senha:
            self.__senha = nova_senha
        else:
            print("Erro: A senha deve ter entre 6 e 15 caracteres e não conter espaços.")

    def setTipoPerfil(self, novo_tipo):
        tipos_permitidos = ["Estudante", "Professor"]
        if novo_tipo in tipos_permitidos:
            self.__tipo_perfil = novo_tipo
        else:
            print("Erro: Tipo de perfil inválido. Escolha 'Estudante' ou 'Professor'.")

    # ==============================
    # MÉTODOS DE NEGÓCIO
    # ==============================
    def validarLogin(self, email_digitado, senha_digitada):
        return self.__email == email_digitado and self.__senha == senha_digitada

    def imprimeInfo(self):
        print("--- Dados do Usuário ---")
        print(f"Nome: {self.getNome()}")
        print(f"E-mail: {self.getEmail()}")
        print(f"Perfil: {self.getTipoPerfil()}")
        print("-" * 24)
