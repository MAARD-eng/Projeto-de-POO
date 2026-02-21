import justpy as jp
from estudante import Estudante
from professor import Professor

# ==========================================
# LÓGICA DE BACKEND (O que acontece ao clicar)
# ==========================================
def cadastrar_usuario(self, msg):
    """
    Esta função roda quando o botão 'Cadastrar' é clicado.
    'self' aqui representa o botão. Usamos self.page para acessar os inputs da tela.
    """
    # 1. Pegando os dados que o usuário digitou na tela web
    nome = self.page.in_nome.value
    email = self.page.in_email.value
    senha = self.page.in_senha.value
    perfil = self.page.in_perfil.value

    # 2. Instanciando a classe correta com base no perfil escolhido
    if perfil == "Estudante":
        curso = self.page.in_curso.value
        matricula = self.page.in_matricula.value
        # Cria o objeto Estudante (passando por todas aquelas suas validações!)
        novo_usuario = Estudante(nome, email, senha, curso, matricula)
    else:
        departamento = self.page.in_dept.value
        titulacao = self.page.in_titulacao.value
        # Cria o objeto Professor
        novo_usuario = Professor(nome, email, senha, departamento, titulacao)

    # 3. PERSISTÊNCIA: Salvando no arquivo de texto (banco de dados simples)
    # O "a" significa 'append' (adicionar ao final do arquivo sem apagar o que já tem)
    with open("banco_usuarios.txt", "a", encoding="utf-8") as arquivo:
        # Salvamos no formato: Perfil,Nome,Email,Senha
        linha = f"{novo_usuario.getTipoPerfil()},{novo_usuario.getNome()},{novo_usuario.getEmail()},{novo_usuario.getSenha()}\n"
        arquivo.write(linha)

    # 4. Feedback visual na tela web
    self.page.div_mensagem.text = f"Sucesso! {novo_usuario.getTipoPerfil()} {novo_usuario.getNome()} cadastrado."
    self.page.div_mensagem.classes = "text-green-600 font-bold mt-4"

    # Limpando os campos após o cadastro
    self.page.in_nome.value = ""
    self.page.in_email.value = ""
    self.page.in_senha.value = ""

# ==========================================
# INTERFACE GRÁFICA WEB (Frontend com JustPy)
# ==========================================
def pagina_cadastro():
    wp = jp.WebPage()
    
    # Usando classes do Tailwind CSS (embutido no JustPy) para deixar bonito
    container = jp.Div(classes="max-w-md mx-auto mt-10 p-6 bg-gray-100 rounded shadow-md", a=wp)
    
    jp.Div(text="Plataforma Universitária", classes="text-2xl font-bold text-center mb-6", a=container)
    jp.Div(text="Crie sua conta:", classes="text-lg mb-4", a=container)

    # Campos Comuns (Da classe Usuario)
    wp.in_nome = jp.Input(placeholder="Seu Nome Completo", classes="w-full border p-2 mb-2 rounded", a=container)
    wp.in_email = jp.Input(placeholder="Seu E-mail", classes="w-full border p-2 mb-2 rounded", a=container)
    wp.in_senha = jp.Input(placeholder="Sua Senha", type="password", classes="w-full border p-2 mb-4 rounded", a=container)

    # Dropdown para escolher o Perfil
    jp.Div(text="Você é:", classes="font-semibold mb-1", a=container)
    wp.in_perfil = jp.Select(classes="w-full border p-2 mb-4 rounded", a=container)
    wp.in_perfil.add(jp.Option(value="Estudante", text="Estudante"))
    wp.in_perfil.add(jp.Option(value="Professor", text="Professor"))

    # Campos Específicos (Para simplificar nesta primeira versão, deixamos todos visíveis)
    jp.Div(text="Dados Específicos:", classes="font-semibold mt-4 mb-1", a=container)
    wp.in_curso = jp.Input(placeholder="Curso (Se for Estudante)", classes="w-full border p-2 mb-2 rounded", a=container)
    wp.in_matricula = jp.Input(placeholder="Matrícula (Se for Estudante)", classes="w-full border p-2 mb-2 rounded", a=container)
    
    wp.in_dept = jp.Input(placeholder="Departamento (Se for Professor)", classes="w-full border p-2 mb-2 rounded", a=container)
    wp.in_titulacao = jp.Select(classes="w-full border p-2 mb-4 rounded", a=container)
    for t in ["Especialista", "Mestre", "Doutor", "Pós-Doutor"]:
        wp.in_titulacao.add(jp.Option(value=t, text=t))

    # Botão de Cadastrar
    btn = jp.Button(text="Concluir Cadastro", classes="w-full bg-blue-600 text-white font-bold py-2 px-4 rounded hover:bg-blue-700", a=container)
    
    # Conectando o botão com a nossa página e com a função que salva os dados
    btn.page = wp 
    btn.on('click', cadastrar_usuario)

    # Divisão invisível que só aparece para mostrar a mensagem de sucesso ou erro
    wp.div_mensagem = jp.Div(text="", classes="", a=container)

    return wp

# ==========================================
# RODANDO O SERVIDOR WEB
# ==========================================
# Esta linha liga o framework JustPy
jp.justpy(pagina_cadastro)
