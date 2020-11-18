from marshmallow import Schema, fields
from .dominios import EscolaSchema, SponsorSchema, AnoEnsinoMedioSchema


class AlunoSchema(Schema):
    id = fields.Int(allow_none=False)
    nome = fields.Str(allow_none=False)
    sobrenome = fields.Str(allow_none=False)
    email = fields.Email(allow_none=False)
    inativo = fields.Boolean(allow_none=False)
    escola = fields.Nested(EscolaSchema, allow_none=False)
    sponsor = fields.Nested(SponsorSchema, allow_none=False)
    ano_ensino_medio = fields.Nested(
        AnoEnsinoMedioSchema, allow_none=False)
