from ..factory.db_injection import injetar_db
from .base import DAOBase
from ..models.ano_ensino_medio import AnoEnsinoMedio


class AnoEnsinoMedioDAOException(BaseException):
    def __init__(self, msg):
        super(AnoEnsinoMedioDAOException, self).__init__(msg)


class AnoEnsinoMedioDAO(DAOBase):
    @injetar_db("instancia_db")
    def __init__(self, instancia_db=None):
        self.db = instancia_db
        if self.db is not None:
            self.db.bind([AnoEnsinoMedio])

    def obter_todos(self):
        try:
            results = list(map(
                lambda ano_em: ano_em.to_dict(),
                AnoEnsinoMedio.select()
            ))
            return results
        except BaseException as e:
            raise AnoEnsinoMedioDAOException(
                f"Error em AnoEnsinoMedioDAO.obter_todos: {e}")

    def salvar(self):
        pass
