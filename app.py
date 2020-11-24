from flask import request
from teu_futuro import (
    TurmaController,
    ProfessorController,
    AlunoController,
    AtividadeController,
    DominiosController,
    RankingGamificacaoController,
    AuthController
)
from config import ConfigurationManager

app = ConfigurationManager.inicializar()


# =============== GETs ===============
@app.route("/turmas")
@AuthController.token_required
def get_all_turmas():
    return TurmaController.obter_todas_turmas()


@app.route("/turma/<int:turma_id>")
@AuthController.token_required
def get_turma(turma_id):
    return TurmaController.obter_turma(turma_id)


@app.route("/professores")
@AuthController.token_required
def get_all_professores():
    return ProfessorController.obter_todos_professores()


@app.route("/escolas")
@AuthController.token_required
def get_all_escolas():
    return DominiosController.obter_todas_escolas()


@app.route("/sponsors")
@AuthController.token_required
def get_all_sponsors():
    return DominiosController.obter_todos_sponsors()


@app.route("/anos-ensino-medio")
@AuthController.token_required
def get_all_anos_ensino_medio():
    return DominiosController.obter_todos_anos_ensino_medio()


@app.route("/turma/<int:turma_id>/alunos")
@AuthController.token_required
def get_all_alunos(turma_id):
    return AlunoController.obter_todos_alunos(turma_id)


@app.route("/turma/<int:turma_id>/atividades")
@AuthController.token_required
def get_all_atividades(turma_id):
    return AtividadeController.obter_todas_atividades(turma_id)


# =============== PUTs ===============
@app.route(
    "/aluno/<int:aluno_id>/inativar", methods=["PUT"])
@AuthController.token_required
def put_inativar_aluno(aluno_id):
    return AlunoController.inativar_aluno(aluno_id)


# =============== POSTs ===============
@app.route("/turma", methods=["POST"])
@AuthController.token_required
def post_turma():
    return TurmaController.criar_turma(request.json)


@app.route("/turma/<int:turma_id>/aluno", methods=["POST"])
@AuthController.token_required
def post_aluno_turma(turma_id):
    return AlunoController.cadastrar_aluno(turma_id, request.json)


@app.route("/turma/<int:turma_id>/atividade", methods=["POST"])
@AuthController.token_required
def post_atividade_turma(turma_id):
    return AtividadeController.cadastrar_atividade(turma_id, request.json)


@app.route(
    "/aluno/<int:aluno_id>/atividade/<int:atividade_id>", methods=["POST"])
@AuthController.token_required
def post_atividade_aluno(aluno_id, atividade_id):
    return AtividadeController.salvar_atividade_aluno(
        aluno_id,
        atividade_id,
        request.json
    )


@app.route(
    "/turma/<int:turma_id>/ranking-gamificacao", methods=["GET", "POST"])
@AuthController.token_required
def ranking_gamificacao_route(turma_id):
    request_methods_actions = {
        "GET": lambda turma_id: RankingGamificacaoController.obter_ranking(
            turma_id,
            request.args.get("aluno_email")
        ),
        "POST": lambda turma_id:
            RankingGamificacaoController.atualizar_ranking(turma_id)
    }
    return request_methods_actions[request.method](turma_id)


@app.route("/login", methods=["POST"])
def auth_route():
    return AuthController.obtem_credenciais(request.authorization)


@app.route("/criar-usuario", methods=["POST"])
def post_criar_usuario():
    return AuthController.criar_novo_usuario(request.json)


if __name__ == "__main__":
    app.run(port=5000)
