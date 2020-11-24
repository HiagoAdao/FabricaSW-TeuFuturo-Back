from peewee import Model, AutoField, TextField
from ..custom_fields.json import JSONField


class Perfil(Model):
    id = AutoField()
    nome = TextField(column_name="NOME")
    permissoes = JSONField(column_name="PERMISSOES")

    def to_dict(self):
        return dict(
            nome=self.nome,
            permissoes=self.permissoes
        )

    @staticmethod
    def from_dict(item_dict: dict):
        return Perfil(**item_dict)

    class Meta:
        table_name = "PERFIL"
