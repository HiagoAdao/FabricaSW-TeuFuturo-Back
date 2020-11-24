from teu_futuro.database import AtividadeDAO


class AtividadeService:
    def __init__(self):
        self.dao = AtividadeDAO()

    def obter_atividade_por_turma(self, turma_id):
        atividades_por_turma = self.dao.obter_todos(turma_id)
        return atividades_por_turma

    def cadastrar_atividade_na_turma(self, turma_id, dados_atividade):
        dados_atividade["turma"] = turma_id
        nova_atividade = self.dao.salvar(dados_atividade)
        return (
            f"Atividade '{nova_atividade['nome']}' "
            f"adicionada na turma {turma_id} com sucesso"
        )

    def adicionar_atividade_aluno(self,
                                  aluno_id,
                                  atividade_id,
                                  resolucao_atividade):
        resolucao_atividade["aluno"] = aluno_id
        resolucao_atividade["atividade"] = atividade_id
        self.dao.salvar_atividade_aluno(resolucao_atividade)
        return "Atividade entregue com sucesso"

    def obter_atividades_aprovadas(self):
        atividades_aprovadas = self.dao.obter_atividades_aprovadas()
        return atividades_aprovadas
