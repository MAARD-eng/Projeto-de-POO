import json
import os

from modelo.estudante import Estudante
from modelo.professor import Professor


class Cadastro:

    def __init__(self, arquivo):

        self.__arquivo = arquivo
        self.__usuarios = []

        self.carregar()


    # =========================
    # GERAR MATRÍCULA AUTOMÁTICA
    # =========================

    def gerar_matricula(self):

        if not self.__usuarios:
            return "0001"

        maior = max(
            int(usuario.getMatricula())
            for usuario in self.__usuarios
            if usuario.getMatricula() is not None
        )

        nova = maior + 1

        return str(nova).zfill(4)


    # =========================
    # INSERIR
    # =========================

    def inserir(self, usuario):

        matricula = self.gerar_matricula()

        usuario.setMatricula(matricula)

        self.__usuarios.append(usuario)

        self.salvar()

        return matricula


    # =========================
    # LISTAR
    # =========================

    def listar(self):

        return self.__usuarios


    # =========================
    # BUSCAR
    # =========================

    def buscar(self, matricula):

        for usuario in self.__usuarios:

            if usuario.getMatricula() == matricula:

                return usuario

        raise ValueError("Usuário não encontrado")


    # =========================
    # REMOVER
    # =========================

    def remover(self, matricula):

        usuario = self.buscar(matricula)

        self.__usuarios.remove(usuario)

        self.salvar()


    # =========================
    # SALVAR
    # =========================

    def salvar(self):

        dados = [usuario.to_dict() for usuario in self.__usuarios]

        with open(self.__arquivo, "w", encoding="utf-8") as f:

            json.dump(dados, f, indent=4, ensure_ascii=False)


    # =========================
    # CARREGAR
    # =========================

    def carregar(self):

        if not os.path.exists(self.__arquivo):
            return

        with open(self.__arquivo, "r", encoding="utf-8") as f:

            dados = json.load(f)

        for d in dados:

            if d["tipo"] == "Estudante":

                usuario = Estudante(
                    d["nome"],
                    d["email"],
                    d["senha"],
                    d["telefone"],
                    d["matricula"],
                    d["curso"]
                )

            elif d["tipo"] == "Professor":

                usuario = Professor(
                    d["nome"],
                    d["email"],
                    d["senha"],
                    d["telefone"],
                    d["matricula"],
                    d["titulacao"]
                )

            else:
                continue

            self.__usuarios.append(usuario)
