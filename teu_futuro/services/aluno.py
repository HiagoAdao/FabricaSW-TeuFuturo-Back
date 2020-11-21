from teu_futuro.database import AlunoDAO


class AlunoService:
    def __init__(self):
        self.dao = AlunoDAO()

    def obter_alunos_por_turma(self, turma_id):
        alunos = self.dao.obter_todos(turma_id)
        return alunos

    def cadastrar_aluno_na_turma(self, turma_id, dados_aluno):
        dados_aluno["turma"] = turma_id
        dados_aluno["escola"] = dados_aluno["escola"]["id"]
        dados_aluno["ano_ensino_medio"] = \
            dados_aluno["ano_ensino_medio"]["id"]
        dados_aluno["sponsor"] = \
            dados_aluno["sponsor"]["id"]

        novo_aluno = self.dao.salvar(dados_aluno)
        return (
            f"Aluno '{novo_aluno['nome']} {novo_aluno['sobrenome']}' "
            f"adicionado na turma {turma_id} com sucesso"
        )

    def inativar_aluno(self, aluno_id):
        aluno = self.dao.inativar(aluno_id)
        return (
            f"Aluno '{aluno['nome']} {aluno['sobrenome']}' "
            "inativado com sucesso"
        )
