from teu_futuro.database import UsuarioDAO
from flask import current_app
from jwt import encode as encode_token
from werkzeug.security import generate_password_hash, check_password_hash


class AuthService:
    def __init__(self):
        self.dao = UsuarioDAO()

    def obter_permissoes_usuario(self, email_usuario):
        permissoes_usuario = self.dao.obter_usuario_por_email(email_usuario)

        if not permissoes_usuario:
            raise Exception("Usuário inexistente")

        turma_id = None
        if permissoes_usuario["perfil"]["nome"] == "aluno":
            turma_id = self.dao.obter_aluno_por_email(email_usuario)

        return { **permissoes_usuario, "turma_id": turma_id }

    def verfica_acesso_usuario(self, permissoes_usuario, senha_usuario):
        is_valid = check_password_hash(
            permissoes_usuario["senha"],
            senha_usuario
        )
        if not is_valid:
            raise Exception("Usuário ou senha inválidos")

        token = encode_token(
            dict(
                usuario=permissoes_usuario["email"],
                turma_id=permissoes_usuario.get("turma_id"),
                perfil=permissoes_usuario["perfil"]
            ),
            current_app.config["SECRET_KEY"]
        )

        return token.decode("UTF-8")

    def criar_usuario_com_permissoes(self, dados_usuario):
        perfil = self.dao.obter_perfil_por_nome(dados_usuario["perfil"])
        dados_usuario["perfil"] = perfil
        dados_usuario["senha"] = generate_password_hash(
            dados_usuario["senha"])

        usuario = self.dao.salvar(dados_usuario)
        return usuario
