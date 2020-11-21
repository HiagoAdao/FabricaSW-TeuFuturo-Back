from teu_futuro.database import AtividadeDAO


class AtividadeService:
    def __init__(self):
        self.dao = AtividadeDAO()

    def obter_atividade_por_turma(self, turma_id):
        atividades = self.dao.obter_todos(turma_id)
        return atividades

    def cadastrar_atividade_na_turma(self, turma_id, dados_atividade):
        dados_atividade["turma"] = turma_id
        nova_atividade = self.dao.salvar(dados_atividade)
        return (
            f"Atividade '{nova_atividade['nome']}' "
            f"adicionada na turma {turma_id} com sucesso"
        )
