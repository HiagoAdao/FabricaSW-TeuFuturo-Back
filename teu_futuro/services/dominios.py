from teu_futuro.database import EscolaDAO, SponsorDAO, AnoEnsinoMedioDAO


class DominiosService:
    def __init__(self):
        self.escola_dao = EscolaDAO()
        self.sponsor_dao = SponsorDAO()
        self.ano_em_dao = AnoEnsinoMedioDAO()

    def obter_escolas(self):
        escolas = self.escola_dao.obter_todos()
        return escolas
