from usuario import Usuario

class Professor:
  def __init__(self, nome, matricula, email, senha):
    Usuario.__init__(self, nome, matricula, email, senha)
