USE teufuturo;

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

create table PERFIL
(
    ID int unsigned auto_increment primary key,
    NOME varchar(50) not null,
    PERMISSOES json not null
);

create table USUARIO
(
    ID int unsigned auto_increment primary key,
    EMAIL varchar(50) not null,
    SENHA varchar(125) not null,
    PERFIL_ID int unsigned not null,
    constraint FK_USUARIO_PERFIL
        foreign key (PERFIL_ID) references PERFIL(ID)
);


-- ---------- CRIANDO PERFIL DE ADMINISTRADOR ----------
INSERT INTO PERFIL (ID, NOME, PERMISSOES) 
VALUES (
    1,
    'administrador',
    '{
        "api": [
            "/turmas",
            "/turma",
            "/turma/<int:turma_id>",
            "/turma/<int:turma_id>/alunos",
            "/turma/<int:turma_id>/atividades",
            "/turma/<int:turma_id>/aluno",
            "/turma/<int:turma_id>/atividade",
            "/turma/<int:turma_id>/ranking-gamificacao",
            "/aluno/<int:aluno_id>/inativar",
            "/professores",
            "/escolas",
            "/sponsors",
            "/anos-ensino-medio"
        ],
        "app": [
            "/turmas",
            "/turma/{id}",
            "/alunos",
            "/atividades",
            "/ranking"
        ]
    }'
);

-- ---------- CRIANDO PERFIL DE PROFESSOR ----------
INSERT INTO PERFIL (ID, NOME, PERMISSOES) 
VALUES (
    2,
    'professor',
    '{
        "api": [
            "/turmas",
            "/turma/<int:turma_id>",
            "/turma/<int:turma_id>/alunos",
            "/turma/<int:turma_id>/atividades",
            "/aluno/<int:aluno_id>/atividade/<int:atividade_id>/aprovar",
            "/turma/<int:turma_id>/ranking-gamificacao"
        ],
        "app": [
            "/turmas",
            "/turma/{id}",
            "/alunos",
            "/atividades",
            "/ranking"
        ]
    }'
);

-- ---------- CRIANDO PERFIL DE ALUNO ----------
INSERT INTO PERFIL (ID, NOME, PERMISSOES) 
VALUES (
    3,
    'aluno',
    '{
        "api": [
            "/turma/<int:turma_id>",
            "/turma/<int:turma_id>/atividades",
            "/turma/<int:turma_id>/ranking-gamificacao",
            "/aluno/<int:aluno_id>/atividade/<int:atividade_id>"
        ],
        "app": [
            "/turma/{id}",
            "/atividades",
            "/ranking"
        ]
    }'
);
