from marshmallow import Schema, fields


class UsuarioSchema(Schema):
    email = fields.Str(allow_none=False)
    senha = fields.Str(allow_none=False)
    perfil = fields.Str(allow_none=False)
