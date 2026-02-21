import justpy as jp
import os
from estudante import Estudante
from professor import Professor

# ==========================================
# FUNÇÃO DE INTERATIVIDADE (Esconder/Mostrar)
# ==========================================
async def mudar_perfil(self, msg):
    """
    Esta função roda sempre que o usuário muda a opção no Select.
    'self.value' será "Estudante" ou "Professor".
    """
    if self.value == "Estudante":
        # Mostra a parte do estudante (tirando o 'hidden') e esconde a do professor
        self.page.div_estudante.classes = self.page.div_estudante.classes.replace("hidden", "").strip()
        if "hidden" not in self.page.div_professor.classes:
            self.page.div_professor.classes += " hidden"
    else:
        # Mostra a parte do professor e esconde a do estudante
        self.page.div_professor.classes = self.page.div_professor.classes.replace("hidden", "").strip()
        if "hidden" not in self.page.div_estudante.classes:
            self.page.div_estudante.classes += " hidden"

# ==========================================
# LÓGICA DE BACKEND (Salvar Dados)
# ==========================================
async def cadastrar_usuario(self, msg):
    try:
        nome = self.page.in_nome.value
        email = self.page.in_email.value
        senha = self.page.in_senha.value
        perfil = self.page.in_perfil.value

        # Pega os dados dependendo de quem está visível
        if perfil == "Estudante":
            curso = self.page.in_curso.value
            matricula = self.page.in_matricula.value
            novo_usuario = Estudante(nome, email, senha, curso, matricula)
        else:
            departamento = self.page.in_dept.value
            titulacao = self.page.in_titulacao.value
            novo_usuario = Professor(nome, email, senha, departamento, titulacao)

        # Salvando no arquivo (com a proteção contra o OneDrive)
        pasta_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_arquivo = os.path.join(pasta_atual, "banco_usuarios.txt")

        with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
            linha = f"{novo_usuario.getTipoPerfil()},{novo_usuario.getNome()},{novo_usuario.getEmail()},{novo_usuario.getSenha()}\n"
            arquivo.write(linha)

        # Mensagem Visual de Sucesso
        self.page.div_mensagem.text = f"Sucesso! {novo_usuario.getTipoPerfil()} {novo_usuario.getNome()} cadastrado."
        self.page.div_mensagem.classes = "text-green-600 font-bold mt-4 block p-2 bg-green-100 rounded"

        # Limpando os campos principais para o próximo cadastro
        self.page.in_nome.value = ""
        self.page.in_email.value = ""
        self.page.in_senha.value = ""

    except Exception as erro:
        self.page.div_mensagem.text = f"ERRO: {erro}"
        self.page.div_mensagem.classes = "text-red-600 font-bold mt-4 block p-2 bg-red-100 rounded"


# ==========================================
# INTERFACE GRÁFICA WEB
# ==========================================
def pagina_cadastro():
    wp = jp.WebPage()
    
    container = jp.Div(classes="max-w-md mx-auto mt-10 p-6 bg-gray-100 rounded shadow-md", a=wp)
    jp.Div(text="Plataforma Universitária", classes="text-2xl font-bold text-center mb-6", a=container)
    
    # === SESSÃO GERAL (Sempre visível) ===
    jp.Div(text="Dados Básicos:", classes="text-lg mb-2 font-semibold", a=container)
    wp.in_nome = jp.Input(placeholder="Seu Nome Completo", classes="w-full border p-2 mb-2 rounded", a=container)
    wp.in_email = jp.Input(placeholder="Seu E-mail", classes="w-full border p-2 mb-2 rounded", a=container)
    wp.in_senha = jp.Input(placeholder="Sua Senha", type="password", classes="w-full border p-2 mb-4 rounded", a=container)

    jp.Div(text="Você é:", classes="font-semibold mb-1", a=container)
    wp.in_perfil = jp.Select(classes="w-full border p-2 mb-4 rounded", a=container)
    wp.in_perfil.add(jp.Option(value="Estudante", text="Estudante"))
    wp.in_perfil.add(jp.Option(value="Professor", text="Professor"))
    
    # Conectando o evento de mudança (change) ao select
    wp.in_perfil.on('change', mudar_perfil)

    # === SESSÃO ESTUDANTE (Visível por padrão) ===
    # Note que guardamos esta Div inteira dentro de wp.div_estudante
    wp.div_estudante = jp.Div(classes="mb-4", a=container)
    jp.Div(text="Dados Acadêmicos (Estudante):", classes="font-semibold mb-1", a=wp.div_estudante)
    wp.in_curso = jp.Input(placeholder="Qual o seu curso?", classes="w-full border p-2 mb-2 rounded", a=wp.div_estudante)
    wp.in_matricula = jp.Input(placeholder="Sua Matrícula", classes="w-full border p-2 mb-2 rounded", a=wp.div_estudante)
    
    # === SESSÃO PROFESSOR (Inicia invisível com a classe 'hidden') ===
    wp.div_professor = jp.Div(classes="mb-4 hidden", a=container)
    jp.Div(text="Dados Acadêmicos (Professor):", classes="font-semibold mb-1", a=wp.div_professor)
    wp.in_dept = jp.Input(placeholder="Seu Departamento", classes="w-full border p-2 mb-2 rounded", a=wp.div_professor)
    wp.in_titulacao = jp.Select(classes="w-full border p-2 rounded", a=wp.div_professor)
    for t in ["Especialista", "Mestre", "Doutor", "Pós-Doutor"]:
        wp.in_titulacao.add(jp.Option(value=t, text=t))

    # === BOTÃO E MENSAGENS ===
    btn = jp.Button(text="Concluir Cadastro", classes="w-full bg-blue-600 text-white font-bold py-2 px-4 rounded hover:bg-blue-700 mt-2", a=container)
    btn.page = wp 
    btn.on('click', cadastrar_usuario)

    wp.div_mensagem = jp.Div(text="", classes="hidden", a=container)

    return wp

jp.justpy(pagina_cadastro)
