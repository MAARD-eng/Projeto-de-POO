import json
from modelo.estudante import Estudante
from modelo.professor import Professor

class Cadastro:
    def __init__(self, arquivo):
        self.__arquivo = arquivo
        self.__usuarios = self.carregar_usuarios()

    def inserir(self, usuario):
        if self.__existe_matricula(usuario.getMatricula()):
            raise ValueError("Matrícula já cadastrada.")

        self.__usuarios.append(usuario)
        self.salvar()

    def remover(self, matricula):
        usuario = self.buscar(matricula)
        self.__usuarios.remove(usuario)
        self.salvar()

    def buscar(self, matricula):
        for usuario in self.__usuarios:
            if usuario.getMatricula() == matricula:
                return usuario

        raise ValueError("Usuário não encontrado.")

    def listar(self):
        return self.__usuarios.copy()
    
    def salvar(self):
        lista_dict = [usuario.to_dict() for usuario in self.__usuarios]

        with open(self.__arquivo, "w", encoding="utf-8") as f:
            json.dump({"usuarios": lista_dict}, f, indent=4, ensure_ascii=False)

    def carregar_usuarios(self):
        try:
            with open(self.__arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)

            lista = []

            for item in dados.get("usuarios", []):
                
                if item["tipo"] == "Professor":
                    usuario = Professor(
                        item["nome"],
                        item["email"],
                        item["senha"],
                        item["telefone"],
                        item["matricula"],
                        item["titulacao"]
                    )

                elif item["tipo"] == "Estudante":
                    usuario = Estudante(
                        item["nome"],
                        item["email"],
                        item["senha"],
                        item["telefone"],
                        item["matricula"],
                        item["curso"]
                    )

                else:
                    continue  # ignora tipo desconhecido

                lista.append(usuario)

            return lista

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            # Arquivo corrompido ou vazio
            return []
    
    def __existe_matricula(self, matricula):
        for usuario in self.__usuarios:
            if usuario.getMatricula() == matricula:
                return True
        return False