from marshmallow import Schema, fields
from .professor import ProfessorSchema


class TurmaSchema(Schema):
    id = fields.Int(allow_none=False)
    nome = fields.Str(allow_none=False)
    professores = fields.Nested(ProfessorSchema, many=True, allow_none=False)
    data_inicio = fields.String(allow_none=False)
    data_fim = fields.String(allow_none=False)
    data_atualizacao_ranking = fields.String(allow_none=True)
