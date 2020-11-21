from ..factory.db_injection import injetar_db
from .base import DAOBase
from ..models.turma import Turma
from ..models.aluno import Aluno
from ..models.atividade import Atividade
from ..models.atividade_aluno import AtividadeAluno


class AtividadeDAOException(BaseException):
    def __init__(self, msg):
        super(AtividadeDAOException, self).__init__(msg)


class AtividadeDAO(DAOBase):
    @injetar_db("instancia_db")
    def __init__(self, instancia_db=None):
        self.db = instancia_db
        if self.db is not None:
            self.db.bind([
                Turma,
                Atividade,
                Aluno,
                AtividadeAluno
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
            raise AtividadeDAOException(
                f"Erro em AtividadeDAO.obter_todos: {e}")

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
                raise AtividadeDAOException(
                    f"Erro em AtividadeDAO.salvar: {e}")

    def salvar_atividade_aluno(self, dados_atividade_aluno):
        with self.db.atomic() as transaction:
            try:
                atividade_aluno = AtividadeAluno.from_dict(
                    dados_atividade_aluno)
                atividade_aluno.save()

                transaction.commit()
            except BaseException as e:
                if transaction is not None:
                    transaction.rollback()
                raise AtividadeDAOException(
                    f"Erro em AtividadeDAO.salvar_atividade_aluno: {e}")
