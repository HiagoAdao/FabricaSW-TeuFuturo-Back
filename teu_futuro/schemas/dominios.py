from marshmallow import Schema, fields


class EscolaSchema(Schema):
    id = fields.Int(allow_none=False)
    nome = fields.Str(allow_none=False)


class SponsorSchema(Schema):
    id = fields.Int(allow_none=False)
    nome = fields.Str(allow_none=False)


class AnoEnsinoMedioSchema(Schema):
    id = fields.Int(allow_none=False)
    ano = fields.Str(allow_none=False)
