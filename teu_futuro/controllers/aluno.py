from teu_futuro.responses import Responses
from teu_futuro.services.aluno import AlunoService
from teu_futuro.schemas.aluno import AlunoSchema


class AlunoController:
    @staticmethod
    def inativar_aluno(aluno_id):
        try:
            aluno_service = AlunoService()
            resp = aluno_service.inativar_aluno(aluno_id)
            return Responses.success(resp)
        except BaseException:
            return Responses.bad_request("Aluno inexistente")

    @staticmethod
    def obter_todos_alunos(turma_id):
        try:    
            aluno_service, aluno_schema = AlunoService(), AlunoSchema()
            alunos = aluno_service.obter_alunos_por_turma(turma_id)
            resp = [aluno_schema.load(aluno) for aluno in alunos]
            return Responses.success(resp)
        except BaseException as err:
            return Responses.bad_request(err)

    @staticmethod
    def cadastrar_aluno(turma_id, request_body):
        try:
            aluno_service, aluno_schema = AlunoService(), AlunoSchema()
            dados_aluno = aluno_schema.dump(request_body)
            resp = aluno_service.cadastrar_aluno_na_turma(
                turma_id, dados_aluno)
            return Responses.created(resp)
        except BaseException as err:
            return Responses.bad_request(err)
