from teu_futuro.responses import Responses
from teu_futuro.services.atividade import AtividadeService
from teu_futuro.services.ranking_gamificacao import RankingGamificacaoService
from teu_futuro.schemas.ranking_gamificacao import RankingGamificacaoSchema


class RankingGamificacaoController:
    @staticmethod
    def obter_ranking(turma_id, aluno_email):
        try:
            gamificacao_service = RankingGamificacaoService()
            gamificacao_schema = RankingGamificacaoSchema()
            ranking_alunos = gamificacao_service.obter_ranking_gamificacao(
                turma_id,
                aluno_email
            )
            resp = [gamificacao_schema.load(ranking_aluno)
                    for ranking_aluno in ranking_alunos]
            return Responses.success(resp)
        except BaseException as err:
            return Responses.bad_request(str(err))

    @staticmethod
    def atualizar_ranking(turma_id):
        try:
            gamificacao_service = RankingGamificacaoService()
            atividade_service = AtividadeService()
            atividades_aprovadas = \
                atividade_service.obter_atividades_aprovadas()
            resp = gamificacao_service.atualizar_ranking_gamificacao(
                turma_id, atividades_aprovadas
            )
            return Responses.success(resp)
        except BaseException as err:
            return Responses.bad_request(str(err))
