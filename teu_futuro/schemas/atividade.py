from marshmallow import Schema, fields


class AtividadeSchema(Schema):
    id = fields.Int(allow_none=False)
    nome = fields.Str(allow_none=False)
    descricao = fields.Str(allow_none=False)
    peso = fields.Integer(allow_none=False)
