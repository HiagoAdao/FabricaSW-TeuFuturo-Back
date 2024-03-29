from ..factory.db_injection import injetar_db
from .base import DAOBase
from ..models.professor import Professor


class ProfessorDAOException(BaseException):
    def __init__(self, msg):
        super(ProfessorDAOException, self).__init__(msg)


class ProfessorDAO(DAOBase):
    @injetar_db("instancia_db")
    def __init__(self, instancia_db=None):
        self.db = instancia_db
        if self.db is not None:
            self.db.bind([Professor])

    def obter_todos(self):
        try:
            results = list(map(
                lambda professor: professor.to_dict(),
                Professor.select()
            ))
            return results
        except BaseException as e:
            raise ProfessorDAOException(
                f"Erro em ProfessorDAO.obter_todos: {e}")

    def salvar(self, dados_professor):
        with self.db.atomic() as transaction:
            try:
                professor = Professor.from_dict(dados_professor)
                professor.save()

                transaction.commit()

                return professor.id
            except BaseException as e:
                if transaction is not None:
                    transaction.rollback()
                raise ProfessorDAOException(
                    f"Erro em ProfessorDAO.salvar: {e}")
