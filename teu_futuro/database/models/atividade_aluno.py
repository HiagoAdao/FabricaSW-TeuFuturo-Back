from peewee import Model, TextField, ForeignKeyField, BooleanField
from .aluno import Aluno
from .atividade import Atividade


class AtividadeAluno(Model):
    aluno = ForeignKeyField(
        Aluno,
        column_name="ALUNO_ID",
    )
    atividade = ForeignKeyField(
        Atividade,
        column_name="ATIVIDADE_ID",
    )
    resolucao = TextField(column_name="RESOLUCAO")
    ind_aprovacao = BooleanField(column_name="IND_APROVACAO", default=False)

    def to_dict(self):
        return dict(
            aluno=self.aluno.to_dict(),
            atividade=self.atividade.to_dict(),
        )

    @staticmethod
    def from_dict(item_dict: dict):
        return AtividadeAluno(**item_dict)

    class Meta:
        table_name = "ATIVIDADE_ALUNO"
