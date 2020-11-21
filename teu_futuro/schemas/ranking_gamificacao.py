from marshmallow import Schema, fields
from .aluno import AlunoSchema


class RankingGamificacaoSchema(Schema):
    posicao = fields.Int(allow_none=False)
    aluno = fields.Nested(AlunoSchema, allow_none=False)
    pontuacao = fields.Float(allow_none=False)
