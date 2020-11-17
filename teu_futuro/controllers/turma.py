from teu_futuro.responses import Responses
from ..services.turma import TurmaService
from ..services.turma_professor import TurmaProfessorService
from ..schemas.turma import TurmaSchema


class TurmaController:
    @staticmethod
    def obter_todas_turmas():
        turma_service, turma_schema = TurmaService(), TurmaSchema()
        turmas = turma_service.obter_turmas()
        resp = [turma_schema.load(turma)
                for turma in turmas]
        return Responses.success(resp)

    @staticmethod
    def obter_turma(turma_id):
        turma_service, turma_schema = TurmaService(), TurmaSchema()
        turma = turma_service.obter_turma(turma_id)
        resp = turma_schema.load(turma)
        return Responses.success(resp)

    @staticmethod
    def criar_turma(request_body):
        turma_service, turma_schema = TurmaService(), TurmaSchema()
        turma_professor_service = TurmaProfessorService()
        try:
            dados_turma = turma_schema.dump(request_body)

            turma_id = turma_service.criar_turma(dados_turma)
            resp = turma_professor_service.salvar_relacionamento(
                turma_id, dados_turma["professores"])

            return Responses.created(resp)
        except BaseException as err:
            return Responses.bad_request(err)
