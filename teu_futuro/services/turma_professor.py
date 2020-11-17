from teu_futuro.database import TurmaProfessorDAO


class TurmaProfessorService:
    def __init__(self):
        self.dao = TurmaProfessorDAO()

    def salvar_relacionamento(self, turma_id, dados_professores):
        for professor in dados_professores:
            self.dao.salvar(
                dict(turma=turma_id, professor=professor["id"])
            )
        return f"Turma {turma_id} criada com sucesso"
