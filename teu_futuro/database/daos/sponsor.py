from ..factory.db_injection import injetar_db
from .base import DAOBase
from ..models.sponsor import Sponsor


class SponsorDAOException(BaseException):
    def __init__(self, msg):
        super(SponsorDAOException, self).__init__(msg)


class SponsorDAO(DAOBase):
    @injetar_db("instancia_db")
    def __init__(self, instancia_db=None):
        self.db = instancia_db
        if self.db is not None:
            self.db.bind([Sponsor])

    def obter_todos(self):
        try:
            results = list(map(
                lambda sponsor: sponsor.to_dict(),
                Sponsor.select()
            ))
            return results
        except BaseException as e:
            raise SponsorDAOException(f"Error em SponsorDAO.obter_todos: {e}")

    def salvar(self):
        pass
