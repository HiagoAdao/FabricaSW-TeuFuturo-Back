from ..factory.db_injection import injetar_db
from .base import DAOBase
from ..models.usuario import Usuario
from ..models.aluno import Aluno
from ..models.perfil import Perfil


class UsuarioDAOException(BaseException):
    def __init__(self, msg):
        super(UsuarioDAOException, self).__init__(msg)


class UsuarioDAO(DAOBase):
    @injetar_db("instancia_db")
    def __init__(self, instancia_db=None):
        self.db = instancia_db
        if self.db is not None:
            self.db.bind([Aluno, Usuario, Perfil])

    def obter_usuario_por_email(self, email_usuario):
        try:
            usuario = Usuario.get_or_none(email=email_usuario)
            return usuario.to_dict() if usuario else None
        except BaseException as e:
            raise UsuarioDAOException(
                f"Error em UsuarioDAO.obter_usuario_por_nome: {e}")

    def obter_perfil_por_nome(self, nome_perfil):
        try:
            perfil = Perfil.get_or_none(nome=nome_perfil)
            return perfil.id if perfil else None
        except BaseException as e:
            raise UsuarioDAOException(
                f"Error em UsuarioDAO.obter_perfil_por_nome: {e}")

    def obter_aluno_por_email(self, email_aluno):
        try:
            aluno = Aluno.get_or_none(email=email_aluno)
            return aluno.turma.id if aluno and aluno.turma else None
        except BaseException as e:
            raise UsuarioDAOException(
                f"Error em UsuarioDAO.obter_aluno_por_email: {e}")

    def obter_todos(self):
        pass

    def salvar(self, dados_usuario):
        with self.db.atomic() as transaction:
            try:
                usuario = Usuario.from_dict(dados_usuario)
                usuario.save()

                transaction.commit()

                return usuario.to_dict()
            except BaseException as e:
                if transaction is not None:
                    transaction.rollback()
                raise UsuarioDAOException(f"Erro em UsuarioDAO.salvar: {e}")
