from teu_futuro.database import ProfessorDAO


class ProfessorService:
    def __init__(self):
        self.dao = ProfessorDAO()

    def obter_professores(self):
        professores = self.dao.obter_todos()
        return professores
