from ..factory.db_injection import injetar_db
from .base import DAOBase
from ..models.atividade import Atividade
from ..models.turma import Turma


class AtividadeDAOException(BaseException):
    def __init__(self, msg):
        super(AtividadeDAOException, self).__init__(msg)


class AtividadeDAO(DAOBase):
    @injetar_db("instancia_db")
    def __init__(self, instancia_db=None):
        self.db = instancia_db
        if self.db is not None:
            self.db.bind([
                Atividade,
                Turma
            ])

    def obter_todos(self, turma_id):
        try:
            query = (
                Atividade
                .select()
                .join(Turma)
                .where((Turma.id == turma_id))
            )
            results = list(map(
                lambda atividade: atividade.to_dict(),
                query
            ))
            return results
        except BaseException as e:
            raise AtividadeDAOException(f"Erro em AtividadeDAO.obter_todos: {e}")

    def salvar(self, dados_atividade):
        with self.db.atomic() as transaction:
            try:
                atividade = Atividade.from_dict(dados_atividade)
                atividade.save()

                transaction.commit()

                return atividade.to_dict()
            except BaseException as e:
                if transaction is not None:
                    transaction.rollback()
                raise AtividadeDAOException(f"Erro em AtividadeDAO.salvar: {e}")
