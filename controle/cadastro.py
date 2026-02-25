import json
import os

from modelo.estudante import Estudante
from modelo.professor import Professor


class Cadastro:

    def __init__(self, arquivo):

        self.__arquivo = arquivo
        self.__usuarios = []

        self.__carregar()


    # =========================
    # GERAR MATRÍCULA AUTOMÁTICA
    # =========================

    def __gerar_matricula(self):

        numero = 1

        if self.__usuarios:

            ultima = self.__usuarios[-1].getMatricula()

            if ultima and ultima.startswith("MAT"):

                parte_numerica = ultima.replace("MAT", "")

                if parte_numerica.isdigit():
                    numero = int(parte_numerica) + 1

        return f"MAT{numero:04d}"


    # =========================
    # INSERIR USUÁRIO
    # =========================

    def inserir(self, usuario):

        # gera matrícula automaticamente
        matricula = self.__gerar_matricula()

        usuario.setMatricula(matricula)

        self.__usuarios.append(usuario)

        self.__salvar()

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

        self.__salvar()


    # =========================
    # SALVAR JSON
    # =========================

    def __salvar(self):

        dados = []

        for usuario in self.__usuarios:

            dados.append(usuario.to_dict())

        with open(self.__arquivo, "w", encoding="utf-8") as f:

            json.dump(dados, f, indent=4, ensure_ascii=False)


    # =========================
    # CARREGAR JSON
    # =========================

    def __carregar(self):

        if not os.path.exists(self.__arquivo):

            return

        with open(self.__arquivo, "r", encoding="utf-8") as f:

            try:

                dados = json.load(f)

            except:

                dados = []

        for item in dados:

            tipo = item.get("tipo")

            if tipo == "Estudante":

                usuario = Estudante(
                    item["nome"],
                    item["email"],
                    item["senha"],
                    item["telefone"],
                    item["matricula"],
                    item["curso"]
                )

            elif tipo == "Professor":

                usuario = Professor(
                    item["nome"],
                    item["email"],
                    item["senha"],
                    item["telefone"],
                    item["matricula"],
                    item["titulacao"]
                )

            else:

                continue

            self.__usuarios.append(usuario)
