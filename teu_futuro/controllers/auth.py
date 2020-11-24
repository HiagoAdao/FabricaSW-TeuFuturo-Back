from teu_futuro.responses import Responses
from teu_futuro.services.auth import AuthService
from teu_futuro.schemas.usuario import UsuarioSchema
from functools import wraps
from jwt import decode as decode_token


class AuthController:
    @staticmethod
    def obtem_credenciais(dados_autenticacao):
        try:

            if not dados_autenticacao.username or \
               not dados_autenticacao.password:
                raise Exception("Basic auth='Login required'")

            auth_service = AuthService()
            permissoes_usuario = auth_service.obter_permissoes_usuario(
                dados_autenticacao.username
            )

            resp = auth_service.verfica_acesso_usuario(
                permissoes_usuario,
                dados_autenticacao.password
            )

            return Responses.success(resp)
        except BaseException as err:
            return Responses.unauthorized(err)

    @staticmethod
    def criar_novo_usuario(request_body):
        try:
            auth_service, usuario_schema = AuthService(), UsuarioSchema()
            dados_usuario = usuario_schema.dump(request_body)

            resp = auth_service.criar_usuario_com_permissoes(dados_usuario)

            return Responses.created(resp)
        except BaseException as err:
            return Responses.bad_request(err)

    @staticmethod
    def token_required(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            from flask import request, current_app
            try:
                current_url = request.url_rule.rule
                current_token = request.headers.get("Authorization")
                if not current_token:
                    return Responses.unauthorized("Token é obrigatório.")

                msg_nao_autorizado = \
                    "Usuário não está autorizado a acessar essa rota"

                usuario = decode_token(
                    current_token,
                    current_app.config["SECRET_KEY"]
                )

                permissoes = usuario["perfil"]["permissoes"]
                if not permissoes:
                    raise Exception(str(msg_nao_autorizado))

                have_access = current_url in permissoes.get("api", [])
                if not have_access:
                    raise Exception(str(msg_nao_autorizado))
            except Exception as err:
                return Responses.unauthorized(str(err)) 
            except BaseException:
                return Responses.unauthorized("Token é inválido.")

            return func(*args, **kwargs)
        return decorator
