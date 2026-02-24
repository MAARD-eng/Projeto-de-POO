import justpy as jp

from modelo.estudante import Estudante
from modelo.professor import Professor
from controle.cadastro import Cadastro


gerenciador = Cadastro("usuarios.json")


# =========================
# EVENTOS
# =========================

async def mudar_perfil(self, msg):

    page = msg.page

    perfil = self.value

    page.in_curso.show = perfil == "Estudante"
    page.in_graduacao.show = perfil == "Professor"

    await page.update()


async def concluir_cadastro(self, msg):

    page = msg.page

    try:

        nome = page.in_nome.value.strip()
        email = page.in_email.value.strip()
        telefone = page.in_telefone.value.strip()

        senha = page.in_senha.value
        confirmar = page.in_confirmar.value

        perfil = page.in_perfil.value


        if senha != confirmar:
            raise ValueError("Senhas não coincidem")


        if perfil == "Estudante":

            curso = page.in_curso.value.strip()

            usuario = Estudante(
                nome,
                email,
                senha,
                telefone,
                None,
                curso
            )


        elif perfil == "Professor":

            graduacao = page.in_graduacao.value.strip()

            usuario = Professor(
                nome,
                email,
                senha,
                telefone,
                None,
                graduacao
            )

        else:

            raise ValueError("Selecione um perfil válido")


        matricula = gerenciador.inserir(usuario)


        page.msg.text = f"Cadastro realizado com sucesso! Matrícula: {matricula}"
        page.msg.classes = "text-green-600 font-bold"
        page.msg.show = True

        limpar_campos(page)


    except Exception as e:

        page.msg.text = str(e)
        page.msg.classes = "text-red-600 font-bold"
        page.msg.show = True


    await page.update()


# =========================
# LIMPAR CAMPOS
# =========================

def limpar_campos(page):

    page.in_nome.value = ""
    page.in_email.value = ""
    page.in_telefone.value = ""
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

    container = jp.Div(a=wp, classes="max-w-lg mx-auto mt-10 p-6 bg-white shadow rounded")

    jp.Div(text="Sistema de Cadastro", a=container, classes="text-2xl mb-4 font-bold")

    wp.in_nome = jp.Input(placeholder="Nome", a=container, classes="w-full p-2 mb-2 border")

    wp.in_email = jp.Input(placeholder="Email", a=container, classes="w-full p-2 mb-2 border")

    wp.in_telefone = jp.Input(placeholder="Telefone", a=container, classes="w-full p-2 mb-2 border")

    wp.in_senha = jp.Input(type="password", placeholder="Senha", a=container, classes="w-full p-2 mb-2 border")

    wp.in_confirmar = jp.Input(type="password", placeholder="Confirmar senha", a=container, classes="w-full p-2 mb-2 border")


    wp.in_perfil = jp.Select(a=container, change=mudar_perfil, classes="w-full p-2 mb-2 border")

    wp.in_perfil.add(jp.Option(value="Selecione...", text="Selecione..."))
    wp.in_perfil.add(jp.Option(value="Estudante", text="Estudante"))
    wp.in_perfil.add(jp.Option(value="Professor", text="Professor"))


    wp.in_curso = jp.Input(placeholder="Curso", a=container, show=False, classes="w-full p-2 mb-2 border")

    wp.in_graduacao = jp.Input(placeholder="Graduação", a=container, show=False, classes="w-full p-2 mb-2 border")


    jp.Button(
        text="Cadastrar",
        click=concluir_cadastro,
        a=container,
        classes="bg-blue-600 text-white p-2 w-full"
    )


    wp.msg = jp.Div(a=container, show=False, classes="mt-3")


    return wp


# =========================
# INICIAR
# =========================

def iniciar():

    jp.justpy(pagina_cadastro)
