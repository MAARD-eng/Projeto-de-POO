import json
import os

from modelo.usuario import Usuario
from modelo.estudante import Estudante
from modelo.professor import Professor


class Cadastro:

    def __init__(self, arquivo):
        self.__arquivo = arquivo
        self.__usuarios = []

        self.__carregar()


    # =========================
    # CARREGAR DO JSON
    # =========================

    def __carregar(self):

        if not os.path.exists(self.__arquivo):
            self.__usuarios = []
            return

        try:
            with open(self.__arquivo, "r", encoding="utf-8") as f:

                dados = json.load(f)

                self.__usuarios = []

                for item in dados:

                    tipo = item.get("tipo")

                    if tipo == "Estudante":

                        usuario = Estudante(
                            item["nome"],
                            item["email"],
                            item["senha"],
                            item["telefone"],
                            item["matricula"],
                            item.get("curso", "")
                        )

                    elif tipo == "Professor":

                        usuario = Professor(
                            item["nome"],
                            item["email"],
                            item["senha"],
                            item["telefone"],
                            item["matricula"],
                            item.get("titulacao", "")
                        )

                    else:

                        usuario = Usuario(
                            item["nome"],
                            item["email"],
                            item["senha"],
                            item["telefone"],
                            item["matricula"]
                        )

                    self.__usuarios.append(usuario)

        except Exception:
            self.__usuarios = []


    # =========================
    # SALVAR NO JSON
    # =========================

    def __salvar(self):

        dados = []

        for usuario in self.__usuarios:
            dados.append(usuario.to_dict())

        with open(self.__arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)


    # =========================
    # INSERIR
    # =========================

    def inserir(self, usuario):

        if self.buscar(usuario.getMatricula(), erro=False) is not None:
            raise ValueError("Matrícula já cadastrada.")

        self.__usuarios.append(usuario)

        self.__salvar()


    # =========================
    # LISTAR
    # =========================

    def listar(self):

        return self.__usuarios


    # =========================
    # BUSCAR
    # =========================

    def buscar(self, matricula, erro=True):

        for usuario in self.__usuarios:

            if usuario.getMatricula() == matricula:
                return usuario

        if erro:
            raise ValueError("Usuário não encontrado.")

        return None


    # =========================
    # REMOVER
    # =========================

    def remover(self, matricula):

        usuario = self.buscar(matricula)

        self.__usuarios.remove(usuario)

        self.__salvar()
