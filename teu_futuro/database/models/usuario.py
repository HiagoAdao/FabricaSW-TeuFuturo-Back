from peewee import Model, AutoField, TextField, ForeignKeyField
from .perfil import Perfil


class Usuario(Model):
    id = AutoField()
    email = TextField(column_name="EMAIL")
    senha = TextField(column_name="SENHA")
    perfil = ForeignKeyField(
        Perfil,
        column_name="PERFIL_ID",
        backref="usuarios"
    )

    def to_dict(self):
        return dict(
            id=self.id,
            email=self.email,
            senha=self.senha,
            perfil=self.perfil.to_dict()
        )

    @staticmethod
    def from_dict(item_dict: dict):
        return Usuario(**item_dict)

    class Meta:
        table_name = "USUARIO"
