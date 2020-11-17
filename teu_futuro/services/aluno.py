class AlunoService:
    def obter_alunos_por_turma(self, turma_id):
        # TODO fazer integração com o banco de dados para obtenção
        # Implementar lógica de inativação (GET em ALUNO)
        # quando tiver banco de dados
        # return TURMAS[turma_id - 1]["alunos"]
        return "Integração com banco de dados a ser criada"

    def cadastrar_aluno_na_turma(self, turma_id, dados_aluno):
        # TODO: Criar lógica de criação quando tiver
        #  conexão com banco de dados
        # dados_aluno["inativo"] = False
        # TURMAS[turma_id - 1]["alunos"].append(dados_aluno)
        # return (
        #     f"Aluno cadastrado na turma "
        #     f"'{TURMAS[turma_id - 1]['nome']}' com sucesso"
        # )
        return "Integração com banco de dados a ser criada"

    def inativar_aluno(self, turma_id, aluno_id):
        # TODO fazer integração com o banco de dados para inativação
        # Implementar lógica de inativação (UPDATE em ALUNO)
        # quando tiver banco de dados
        # aluno = TURMAS[turma_id - 1]["alunos"][aluno_id - 1]
        # aluno["inativo"] = True
        # return (
        #     f"Aluno '{aluno['nome']} {aluno['sobrenome']}' da turma "
        #     f"'{TURMAS[turma_id - 1]['nome']}' inativado com sucesso"
        # )
        return "Integração com banco de dados a ser criada"
