from teu_futuro.responses import Responses
from teu_futuro.schemas.professor import ProfessorSchema
from teu_futuro.services.professor import ProfessorService


class ProfessorController:
    @staticmethod
    def obter_todos_professores():
        professor_service = ProfessorService()
        professor_schema = ProfessorSchema()
        professores = professor_service.obter_professores()
        resp = [professor_schema.load(professor)
                for professor in professores]
        return Responses.success(resp)
