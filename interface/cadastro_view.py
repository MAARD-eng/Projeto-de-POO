import justpy as jp

from modelo.estudante import Estudante
from modelo.professor import Professor
from controle.cadastro import Cadastro


# =========================
# GERENCIADOR GLOBAL
# =========================

gerenciador = Cadastro("usuarios.json")


# =========================
# EXCEÇÕES PERSONALIZADAS
# =========================

class SenhaDivergenteError(Exception):
    pass


class CampoObrigatorioError(Exception):
    pass


class PerfilInvalidoError(Exception):
    pass


# =========================
# EVENTOS
# =========================

async def mudar_perfil(self, msg):

    page = msg.page
    perfil = self.value

    page.in_curso.show = (perfil == "Estudante")
    page.in_graduacao.show = (perfil == "Professor")

    await page.update()


async def concluir_cadastro(self, msg):

    page = msg.page

    try:

        nome = page.in_nome.value.strip()
        email = page.in_email.value.strip()
        telefone = page.in_telefone.value.strip()
        matricula = page.in_matricula.value.strip()
        senha = page.in_senha.value
        confirmar = page.in_confirmar.value
        perfil = page.in_perfil.value


        # =========================
        # VALIDAÇÕES
        # =========================

        if not nome:
            raise CampoObrigatorioError("Nome é obrigatório")

        if not email:
            raise CampoObrigatorioError("Email é obrigatório")

        if not matricula:
            raise CampoObrigatorioError("Matrícula é obrigatória")

        if not senha:
            raise CampoObrigatorioError("Senha é obrigatória")

        if perfil == "Selecione...":
            raise PerfilInvalidoError("Selecione um perfil válido")

        if senha != confirmar:
            raise SenhaDivergenteError("As senhas não coincidem")


        # =========================
        # CRIAÇÃO DO OBJETO
        # =========================

        if perfil == "Estudante":

            curso = page.in_curso.value.strip()

            if not curso:
                raise CampoObrigatorioError("Curso é obrigatório")

            # ✅ ORDEM CORRIGIDA AQUI
            usuario = Estudante(
                nome,
                email,
                senha,
                telefone,
                matricula,
                curso
            )


        elif perfil == "Professor":

            graduacao = page.in_graduacao.value.strip()

            if not graduacao:
                raise CampoObrigatorioError("Graduação é obrigatória")

            usuario = Professor(
                nome,
                email,
                senha,
                telefone,
                matricula,
                graduacao
            )

        else:

            raise PerfilInvalidoError("Perfil inválido")


        # =========================
        # SALVAR NO ARQUIVO
        # =========================

        gerenciador.inserir(usuario)


        # =========================
        # FEEDBACK SUCESSO
        # =========================

        page.msg.text = "Cadastro realizado com sucesso!"
        page.msg.classes = "text-green-600 font-semibold mt-2"
        page.msg.show = True

        limpar_campos(page)


    except Exception as e:

        page.msg.text = str(e)
        page.msg.classes = "text-red-600 font-semibold mt-2"
        page.msg.show = True


    finally:

        await page.update()


# =========================
# FUNÇÃO AUXILIAR
# =========================

def limpar_campos(page):

    page.in_nome.value = ""
    page.in_email.value = ""
    page.in_telefone.value = ""
    page.in_matricula.value = ""
    page.in_senha.value = ""
    page.in_confirmar.value = ""
    page.in_curso.value = ""
    page.in_graduacao.value = ""

    page.in_perfil.value = "Selecione..."

    page.in_curso.show = False
    page.in_graduacao.show = False


# =========================
# INTERFACE
# =========================

def pagina_cadastro():

    wp = jp.WebPage()

    container = jp.Div(
        a=wp,
        classes="""
        max-w-lg mx-auto mt-10
        p-6
        bg-white
        shadow-lg
        rounded-lg
        border-t-4 border-blue-600
        """
    )

    jp.Div(
        text="Sistema de Cadastro",
        a=container,
        classes="text-2xl font-bold mb-6 text-center"
    )


    wp.in_nome = jp.Input(
        placeholder="Nome completo",
        a=container,
        classes="w-full p-2 mb-3 border rounded"
    )

    wp.in_email = jp.Input(
        placeholder="Email",
        a=container,
        classes="w-full p-2 mb-3 border rounded"
    )

    wp.in_telefone = jp.Input(
        placeholder="Telefone",
        a=container,
        classes="w-full p-2 mb-3 border rounded"
    )

    wp.in_matricula = jp.Input(
        placeholder="Matrícula",
        a=container,
        classes="w-full p-2 mb-3 border rounded"
    )


    # SENHAS

    row = jp.Div(
        a=container,
        classes="grid grid-cols-2 gap-2 mb-3"
    )

    wp.in_senha = jp.Input(
        placeholder="Senha",
        type="password",
        a=row,
        classes="p-2 border rounded"
    )

    wp.in_confirmar = jp.Input(
        placeholder="Confirmar senha",
        type="password",
        a=row,
        classes="p-2 border rounded"
    )


    # PERFIL

    wp.in_perfil = jp.Select(
        a=container,
        change=mudar_perfil,
        classes="w-full p-2 mb-3 border rounded"
    )

    for opt in ["Selecione...", "Estudante", "Professor"]:
        wp.in_perfil.add(jp.Option(value=opt, text=opt))

    wp.in_perfil.value = "Selecione..."


    # CAMPOS DINÂMICOS

    wp.in_curso = jp.Input(
        placeholder="Curso",
        a=container,
        show=False,
        classes="w-full p-2 mb-3 border rounded bg-blue-50"
    )

    wp.in_graduacao = jp.Input(
        placeholder="Graduação",
        a=container,
        show=False,
        classes="w-full p-2 mb-3 border rounded bg-green-50"
    )


    # BOTÃO

    jp.Button(
        text="Cadastrar",
        click=concluir_cadastro,
        a=container,
        classes="""
        w-full
        bg-blue-600
        text-white
        font-bold
        py-2
        rounded
        hover:bg-blue-700
        """
    )


    # MENSAGEM

    wp.msg = jp.Div(
        text="",
        a=container,
        show=False
    )


    return wp


# =========================
# EXECUÇÃO
# =========================

def iniciar():

    jp.justpy(pagina_cadastro)


# Permite rodar diretamente

if __name__ == "__main__":

    iniciar()
