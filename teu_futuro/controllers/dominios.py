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