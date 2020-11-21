from teu_futuro.database import RankingGamificacaoDAO


class RankingGamificacaoService:
    def __init__(self):
        self.dao = RankingGamificacaoDAO()

    def obter_ranking_gamificacao(self, turma_id, aluno_id):
        ranking_completo = self.dao.obter_todos(turma_id)

        if not ranking_completo:
            return []

        aluno = next(filter(
            lambda rank: rank["aluno"]["id"] == aluno_id,
            ranking_completo
        ), None)

        classificacao_ranking = [
            {"posicao": posicao + 1, **dados_aluno}
            for posicao, dados_aluno in enumerate(ranking_completo[:10])
        ]
        if aluno not in classificacao_ranking:
            posicao_aluno = ranking_completo.index(aluno) + 1
            classificacao_ranking.append({"posicao": posicao_aluno, **aluno})

        return classificacao_ranking

    def atualizar_ranking_gamificacao(self, turma_id, atividades_alunos):
        dados_ranking = []
        for dado in atividades_alunos:
            aluno_id = dado["aluno"]["id"]
            peso_atividade = dado["atividade"]["peso"]

            aluno_existente = next(filter(
                lambda aluno: aluno["aluno"] == aluno_id,
                dados_ranking
            ), None)

            if not aluno_existente:
                dados_ranking.append(dict(
                    turma=turma_id,
                    aluno=aluno_id,
                    pontuacao=peso_atividade + 1
                ))
            else:
                aluno_existente["pontuacao"] += peso_atividade

        for ranking in dados_ranking:
            self.dao.salvar(ranking)

        return "Ranking atualizado com sucesso"
