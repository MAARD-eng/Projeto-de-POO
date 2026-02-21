class Estudante:
  def __init__(self, nome, email, senha, matricula, curso):
    Usuario.__init__(self, nome, email, senha)
    self.__curso = curso

  def getCurso(self):
    return curso

  def setCurso(self, curso):
    self.__curso = curso
