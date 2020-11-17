from teu_futuro.database import EscolaDAO, SponsorDAO, AnoEnsinoMedioDAO


class DominiosService:
    def __init__(self):
        self.escola_dao = EscolaDAO()
        self.sponsor_dao = SponsorDAO()
        self.ano_em_dao = AnoEnsinoMedioDAO()

    def obter_escolas(self):
        escolas = self.escola_dao.obter_todos()
        return escolas

    def obter_sponsors(self):
        sponsors = self.sponsor_dao.obter_todos()
        return sponsors

    def obter_anos_ensino_medio(self):
        anos_ensino_medio = self.ano_em_dao.obter_todos()
        return anos_ensino_medio
