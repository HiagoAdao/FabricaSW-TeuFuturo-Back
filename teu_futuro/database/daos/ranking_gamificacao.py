from ..factory.db_injection import injetar_db
from .base import DAOBase
from ..models.ranking_gamificacao import RankingGamificacao
from ..models.turma import Turma
from ..models.aluno import Aluno
from datetime import datetime


class RankingGamificacaoDAOException(BaseException):
    def __init__(self, msg):
        super(RankingGamificacaoDAOException, self).__init__(msg)


class RankingGamificacaoDAO(DAOBase):
    @injetar_db("instancia_db")
    def __init__(self, instancia_db=None):
        self.db = instancia_db
        if self.db is not None:
            self.db.bind([
                Turma,
                Aluno,
                RankingGamificacao
            ])

    def obter_todos(self, turma_id):
        try:
            query = (
                RankingGamificacao
                .select(
                    Aluno,
                    RankingGamificacao.pontuacao
                )
                .join(Aluno)
                .switch(RankingGamificacao)
                .join(Turma)
                .where((Turma.id == turma_id))
                .order_by(RankingGamificacao.pontuacao.desc())
            )
            results = list(map(
                lambda ranking: ranking.to_dict(),
                query
            ))
            return results
        except BaseException as e:
            raise RankingGamificacaoDAOException(
                f"Error em RankingGamificacaoDAO.obter_todos: {e}")

    def salvar(self, dados_ranking):
        with self.db.atomic() as transaction:
            try:
                query_update_ranking = (
                    RankingGamificacao
                    .insert(**dados_ranking)
                    .on_conflict('replace')
                )
                query_update_ranking.execute()

                nova_data_atualizacao = datetime.now()
                query_update_data_atualizacao = (
                    Turma
                    .update(
                        data_atualizacao_ranking=nova_data_atualizacao
                    )
                    .where((Turma.id == dados_ranking["turma"]))
                )
                query_update_data_atualizacao.execute()

                transaction.commit()
            except BaseException as e:
                if transaction is not None:
                    transaction.rollback()
                raise RankingGamificacaoDAOException(
                    f"Erro em RankingGamificacaoDAO.salvar: {e}")
