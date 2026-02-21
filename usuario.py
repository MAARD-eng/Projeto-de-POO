class Usuario:
    def __init__(self, nome, email, senha, tipo_perfil):
        # 1. Definimos valores padrão seguros primeiro. 
        # Assim, se a validação falhar, o sistema não quebra e o objeto ganha um valor "reserva".
        self.__nome = "Indefinido"
        self.__email = "indefinido@email.com"
        self.__senha = "000000"
        self.__tipo_perfil = "Estudante" 
        
        # 2. Chamamos os setters para aplicar os valores passando por todas as regras
        self.setNome(nome)
        self.setEmail(email)
        self.setSenha(senha)
        self.setTipoPerfil(tipo_perfil)

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
        # Remove espaços em branco nas pontas e verifica se tem mais de 2 letras
        if len(novo_nome.strip()) > 2:
            self.__nome = novo_nome.strip()
        else:
            print("Erro: O nome deve ter mais de 2 caracteres válidos.")

    def setEmail(self, novo_email):
        # Exige '@', '.' e proíbe espaços em branco. Salva tudo em minúsculo.
        if "@" in novo_email and "." in novo_email and " " not in novo_email:
            self.__email = novo_email.lower()
        else:
            print("Erro: E-mail inválido. Deve conter '@', '.' e não ter espaços.")

    def setSenha(self, nova_senha):
        # Exige entre 6 e 15 caracteres e não permite espaços
        if 6 <= len(nova_senha) <= 15 and " " not in nova_senha:
            self.__senha = nova_senha
        else:
            print("Erro: A senha deve ter entre 6 e 15 caracteres e não conter espaços.")

    def setTipoPerfil(self, novo_tipo):
        # Aceita apenas os perfis principais do escopo do projeto
        tipos_permitidos = ["Estudante", "Professor"]
        if novo_tipo in tipos_permitidos:
            self.__tipo_perfil = novo_tipo
        else:
            print("Erro: Tipo de perfil inválido. Escolha 'Estudante' ou 'Professor'.")

    # ==============================
    # MÉTODOS DE NEGÓCIO
    # ==============================
    def validarLogin(self, email_digitado, senha_digitada):
        """
        Retorna True se o email e a senha baterem. 
        Útil para a Funcionalidade 2 (Login).
        """
        return self.__email == email_digitado and self.__senha == senha_digitada

    def imprimeInfo(self):
        print("--- Dados do Usuário ---")
        print(f"Nome: {self.getNome()}")
        print(f"E-mail: {self.getEmail()}")
        print(f"Perfil: {self.getTipoPerfil()}")
        print("-" * 24)
