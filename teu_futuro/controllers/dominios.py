from teu_futuro.responses import Responses
from teu_futuro.schemas.dominios import (
    EscolaSchema, SponsorSchema, AnoEnsinoMedioSchema
)
from teu_futuro.services.dominios import DominiosService


class DominiosController:
    @staticmethod
    def obter_todas_escolas():
        dominios_service = DominiosService()
        escola_schema = EscolaSchema()
        escolas = dominios_service.obter_escolas()
        resp = [escola_schema.load(escola)
                for escola in escolas]
        return Responses.success(resp)

    @staticmethod
    def obter_todos_sponsors():
        dominios_service = DominiosService()
        sponsor_schema = SponsorSchema()
        sponsors = dominios_service.obter_sponsors()
        resp = [sponsor_schema.load(sponsor)
                for sponsor in sponsors]
        return Responses.success(resp)

    @staticmethod
    def obter_todos_anos_ensino_medio():
        dominios_service = DominiosService()
        ano_ensino_medio_schema = AnoEnsinoMedioSchema()
        anos_ensino_medio = dominios_service.obter_anos_ensino_medio()
        resp = [ano_ensino_medio_schema.load(ano_em)
                for ano_em in anos_ensino_medio]
        return Responses.success(resp)
