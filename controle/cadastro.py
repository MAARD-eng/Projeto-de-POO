import json
from modelo.usuario import Estudante, Professor

class Cadastro:
    def __init__(self, arquivo):
        self.__arquivo = arquivo
        self.__usuarios = self.carregar_usuarios()

    def inserir(self, usuario):
        pass

    def remover(self, matricula):
        pass

    def buscar(self, matricula):
        pass

    def listar(self):
        pass

    def salvar(self):
        pass

    def carregar_usuarios(self):
        try:
            with open(self.__arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)

            lista = []

            for item in dados.get("usuarios", []):
                
                if item["tipo"] == "Professor":
                    usuario = Professor(
                        item["matricula"],
                        item["nome"],
                        item["email"],
                        item["telefone"],
                        item["senha"],
                        item["graduaçao"]
                    )

                elif item["tipo"] == "Aluno":
                    usuario = Estudante(
                        item["matricula"],
                        item["nome"],
                        item["email"],
                        item["telefone"],
                        item["senha"],
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