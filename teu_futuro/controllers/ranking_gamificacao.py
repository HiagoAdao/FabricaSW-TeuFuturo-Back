from teu_futuro.responses import Responses
from teu_futuro.services.atividade import AtividadeService
from teu_futuro.services.ranking_gamificacao import RankingGamificacaoService


class RankingGamificacaoController:
    @staticmethod
    def obter_ranking(turma_id, aluno_id):
        try:
            gamificacao_service = RankingGamificacaoService()
            resp = gamificacao_service.obter_ranking_gamificacao(
                turma_id,
                int(aluno_id)
            )
            return Responses.success(resp)
        except BaseException as err:
            return Responses.bad_request(err)

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
            return Responses.bad_request(err)
