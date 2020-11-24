from teu_futuro.database import TurmaDAO
from ..util.date import Formatos, converte_str_para_datetime


class TurmaService:
    def __init__(self):
        self.dao = TurmaDAO()

    def _obtem_professores_turma(self, turmas_professores):
        turmas = []
        for item in turmas_professores:
            turma_existente = next(filter(
                lambda t: t["id"] == item["turma"]["id"],
                turmas
            ), None)
            if not turma_existente:
                turmas.append({
                    **item["turma"],
                    "professores": [item["professor"]]
                })
            else:
                turma_existente["professores"].append(item["professor"])
        return turmas

    def obter_turmas(self, email_professor):
        if not email_professor:
            turmas_banco = self.dao.obter_todos()
            turmas = self._obtem_professores_turma(turmas_banco)
            return turmas
        turmas_professor = self.dao.obter_turma_por_professor(email_professor)
        turmas = self._obtem_professores_turma(turmas_professor)
        return turmas

    def obter_turma(self, turma_id):
        turma_banco = self.dao.obter(turma_id)
        turma = self._obtem_professores_turma(turma_banco)
        return turma[0] if turma else None

    def criar_turma(self, dados_turma):
        dados_turma["data_inicio"] = converte_str_para_datetime(
            dados_turma["data_inicio"], Formatos.BRASILEIRO.value
        )
        dados_turma["data_fim"] = converte_str_para_datetime(
            dados_turma["data_fim"], Formatos.BRASILEIRO.value
        )
        turma_id = self.dao.salvar(dados_turma)
        return turma_id

    def adicionar_professores_na_turma(self, turma_id, dados_professores):
        for professor in dados_professores:
            self.dao.salvar_professor_na_turma(
                dict(turma=turma_id, professor=professor["id"])
            )
