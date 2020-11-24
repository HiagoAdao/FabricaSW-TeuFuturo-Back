from teu_futuro.responses import Responses
from teu_futuro.services.atividade import AtividadeService
from teu_futuro.schemas.atividade import (
    AtividadeSchema, ResolucaoAtividadeSchema
)


class AtividadeController:
    @staticmethod
    def obter_todas_atividades(turma_id):
        try:
            ativ_service = AtividadeService()
            resp = [
                AtividadeSchema().load(ativ)
                for ativ in ativ_service.obter_atividade_por_turma(turma_id)
            ]
            return Responses.success(resp)
        except BaseException as err:
            return Responses.bad_request(err)

    @staticmethod
    def cadastrar_atividade(turma_id, request_body):
        try:
            atividade_service = AtividadeService()
            atividade_schema = AtividadeSchema()
            dados_atividade = atividade_schema.dump(request_body)
            resp = atividade_service.cadastrar_atividade_na_turma(
                turma_id,
                dados_atividade
            )
            return Responses.created(resp)
        except BaseException as err:
            return Responses.bad_request(str(err))

    @staticmethod
    def salvar_atividade_aluno(aluno_id, atividade_id, request_body):
        try:
            atividade_service = AtividadeService()
            resolucao_atividade_schema = ResolucaoAtividadeSchema()
            dados_resolucao = resolucao_atividade_schema.dump(request_body)
            resp = atividade_service.adicionar_atividade_aluno(
                aluno_id,
                atividade_id,
                dados_resolucao
            )
            return Responses.created(resp)
        except BaseException as err:
            return Responses.bad_request(str(err))

    @staticmethod
    def aprovar_atividade_aluno(aluno_id, atividade_id):
        try:
            atividade_service = AtividadeService()
            resp = atividade_service.aprovar_atividade_aluno(
                aluno_id,
                atividade_id
            )
            return Responses.created(resp)
        except BaseException as err:
            return Responses.bad_request(str(err))
