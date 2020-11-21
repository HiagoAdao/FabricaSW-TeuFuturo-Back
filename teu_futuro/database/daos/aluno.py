from ..factory.db_injection import injetar_db
from .base import DAOBase
from ..models.aluno import Aluno
from ..models.turma import Turma
from ..models.escola import Escola
from ..models.sponsor import Sponsor
from ..models.ano_ensino_medio import AnoEnsinoMedio


class AlunoDAOException(BaseException):
    def __init__(self, msg):
        super(AlunoDAOException, self).__init__(msg)


class AlunoDAO(DAOBase):
    @injetar_db("instancia_db")
    def __init__(self, instancia_db=None):
        self.db = instancia_db
        if self.db is not None:
            self.db.bind([
                Aluno,
                Turma,
                Escola,
                Sponsor,
                AnoEnsinoMedio
            ])

    def obter_todos(self, turma_id):
        try:
            query = (
                Aluno
                .select()
                .join(Turma)
                .where((Turma.id == turma_id))
            )
            results = list(map(lambda aluno: aluno.to_dict(), query))
            return results
        except BaseException as e:
            raise AlunoDAOException(f"Erro em AlunoDAO.obter_todos: {e}")

    def salvar(self, dados_aluno):
        with self.db.atomic() as transaction:
            try:
                aluno = Aluno.from_dict(dados_aluno)
                aluno.save()

                transaction.commit()

                return aluno.to_dict()
            except BaseException as e:
                if transaction is not None:
                    transaction.rollback()
                raise AlunoDAOException(f"Erro em AlunoDAO.salvar: {e}")

    def inativar(self, aluno_id):
        with self.db.atomic() as transaction:
            try:
                query = (
                    Aluno
                    .update(inativo=True)
                    .where((Aluno.id == aluno_id))
                )
                query.execute()

                transaction.commit()
            except BaseException as e:
                if transaction is not None:
                    transaction.rollback()
                raise AlunoDAOException(f"Erro em AlunoDAO.inativar: {e}")
