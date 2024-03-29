from ..factory.db_injection import injetar_db
from .base import DAOBase
from ..models.turma import Turma
from ..models.professor import Professor
from ..models.turma_professor import TurmaProfessor


class TurmaDAOException(BaseException):
    def __init__(self, msg):
        super(TurmaDAOException, self).__init__(msg)


class TurmaDAO(DAOBase):
    @injetar_db("instancia_db")
    def __init__(self, instancia_db=None):
        self.db = instancia_db
        if self.db is not None:
            self.db.bind([
                Turma,
                Professor,
                TurmaProfessor
            ])

    def obter_todos(self):
        try:
            query = (
                TurmaProfessor.select(
                    Turma,
                    Professor
                )
                .join(Turma,
                      on=(Turma.id == TurmaProfessor.turma))
                .switch(TurmaProfessor)
                .join(Professor,
                      on=(Professor.id ==
                          TurmaProfessor.professor))
            )
            return list(map(lambda turma: turma.to_dict(), query))
        except BaseException as e:
            raise TurmaDAOException(f"Erro em TurmaDAO.obter_todos: {e}")

    def obter(self, turma_id):
        try:
            query = (
                TurmaProfessor.select(
                    Turma,
                    Professor
                )
                .join(Turma)
                .switch(TurmaProfessor)
                .join(Professor)
                .where((Turma.id == turma_id))
            )
            return list(map(lambda turma: turma.to_dict(), query))
        except BaseException as e:
            raise TurmaDAOException(f"Erro em TurmaDAO.obter: {e}")

    def obter_turma_por_professor(self, email_professor):
        try:
            query = (
                TurmaProfessor.select(
                    Turma,
                    Professor
                )
                .join(Turma)
                .switch(TurmaProfessor)
                .join(Professor)
                .where((Professor.email == email_professor))
            )
            return list(map(lambda turma: turma.to_dict(), query))
        except BaseException as e:
            raise TurmaDAOException(f"Erro em TurmaDAO.obter: {e}")

    def salvar(self, dados_turma):
        with self.db.atomic() as transaction:
            try:
                turma = Turma.from_dict(dados_turma)
                turma.save()

                transaction.commit()

                return turma.id
            except BaseException as e:
                if transaction is not None:
                    transaction.rollback()
                raise TurmaDAOException(f"Erro em TurmaDAO.salvar: {e}")

    def salvar_professor_na_turma(self, dados_turma_professor):
        with self.db.atomic() as transaction:
            try:
                turma_professor = TurmaProfessor.from_dict(
                    dados_turma_professor)
                turma_professor.save()

                transaction.commit()

                return turma_professor
            except BaseException as e:
                if transaction is not None:
                    transaction.rollback()
                raise TurmaDAOException(
                    f"Erro em TurmaDAO.salvar: {e}")
