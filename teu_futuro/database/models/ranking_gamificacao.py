from peewee import Model, ForeignKeyField, DecimalField
from .turma import Turma
from .aluno import Aluno


class RankingGamificacao(Model):
    turma = ForeignKeyField(Turma, column_name="TURMA_ID")
    aluno = ForeignKeyField(Aluno, column_name="ALUNO_ID")
    pontuacao = DecimalField(column_name="PONTUACAO", default=0.0)

    def to_dict(self):
        return dict(
            aluno=self.aluno.to_dict(),
            pontuacao=float(self.pontuacao)
        )

    @staticmethod
    def from_dict(item_dict: dict):
        return RankingGamificacao(**item_dict)

    class Meta:
        table_name = "RANKING_GAMIFICACAO"
