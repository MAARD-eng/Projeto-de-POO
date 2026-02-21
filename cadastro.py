import justpy as jp
from Estudante import Estudante
from Professor import Professor

# ==========================================
# LÓGICA DE BACKEND (O que acontece ao clicar)
# ==========================================
# Mudança 1: Adicionamos 'async' para a página responder melhor
async def cadastrar_usuario(self, msg):
    # Mudança 2: Adicionamos o try/except. Se o Python der erro, não trava!
    try:
        # 1. Pegando os dados que o usuário digitou
        nome = self.page.in_nome.value
        email = self.page.in_email.value
        senha = self.page.in_senha.value
        perfil = self.page.in_perfil.value

        # 2. Instanciando a classe
        if perfil == "Estudante":
            curso = self.page.in_curso.value
            matricula = self.page.in_matricula.value
            novo_usuario = Estudante(nome, email, senha, curso, matricula)
        else:
            departamento = self.page.in_dept.value
            titulacao = self.page.in_titulacao.value
            novo_usuario = Professor(nome, email, senha, departamento, titulacao)

        # 3. Salvando no arquivo de texto
        with open("banco_usuarios.txt", "a", encoding="utf-8") as arquivo:
            linha = f"{novo_usuario.getTipoPerfil()},{novo_usuario.getNome()},{novo_usuario.getEmail()},{novo_usuario.getSenha()}\n"
            arquivo.write(linha)

        # 4. Mensagem de Sucesso (Fica Verde)
        self.page.div_mensagem.text = f"Sucesso! {novo_usuario.getTipoPerfil()} {novo_usuario.getNome()} cadastrado."
        self.page.div_mensagem.classes = "text-green-600 font-bold mt-4"

        # Limpando os campos
        self.page.in_nome.value = ""
        self.page.in_email.value = ""
        self.page.in_senha.value = ""

    except Exception as erro:
        # 5. Se der erro no Python, ele avisa na tela do site (Fica Vermelho)
        self.page.div_mensagem.text = f"ERRO INTERNO NO PYTHON: {erro}"
        self.page.div_mensagem.classes = "text-red-600 font-bold mt-4 block"

# ==========================================
# INTERFACE GRÁFICA WEB
# ==========================================
def pagina_cadastro():
    wp = jp.WebPage()
    
    container = jp.Div(classes="max-w-md mx-auto mt-10 p-6 bg-gray-100 rounded shadow-md", a=wp)
    jp.Div(text="Plataforma Universitária", classes="text-2xl font-bold text-center mb-6", a=container)
    jp.Div(text="Crie sua conta:", classes="text-lg mb-4", a=container)

    wp.in_nome = jp.Input(placeholder="Seu Nome Completo", classes="w-full border p-2 mb-2 rounded", a=container)
    wp.in_email = jp.Input(placeholder="Seu E-mail", classes="w-full border p-2 mb-2 rounded", a=container)
    wp.in_senha = jp.Input(placeholder="Sua Senha", type="password", classes="w-full border p-2 mb-4 rounded", a=container)

    jp.Div(text="Você é:", classes="font-semibold mb-1", a=container)
    wp.in_perfil = jp.Select(classes="w-full border p-2 mb-4 rounded", a=container)
    wp.in_perfil.add(jp.Option(value="Estudante", text="Estudante"))
    wp.in_perfil.add(jp.Option(value="Professor", text="Professor"))

    jp.Div(text="Dados Específicos:", classes="font-semibold mt-4 mb-1", a=container)
    wp.in_curso = jp.Input(placeholder="Curso (Se for Estudante)", classes="w-full border p-2 mb-2 rounded", a=container)
    wp.in_matricula = jp.Input(placeholder="Matrícula (Se for Estudante)", classes="w-full border p-2 mb-2 rounded", a=container)
    
    wp.in_dept = jp.Input(placeholder="Departamento (Se for Professor)", classes="w-full border p-2 mb-2 rounded", a=container)
    wp.in_titulacao = jp.Select(classes="w-full border p-2 mb-4 rounded", a=container)
    for t in ["Especialista", "Mestre", "Doutor", "Pós-Doutor"]:
        wp.in_titulacao.add(jp.Option(value=t, text=t))

    btn = jp.Button(text="Concluir Cadastro", classes="w-full bg-blue-600 text-white font-bold py-2 px-4 rounded hover:bg-blue-700", a=container)
    btn.page = wp 
    btn.on('click', cadastrar_usuario)

    # Div para mostrar erros ou sucesso
    wp.div_mensagem = jp.Div(text="", classes="", a=container)

    return wp

jp.justpy(pagina_cadastro)
