USE teufuturo;

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

create table RANKING_GAMIFICACAO
(
    TURMA_ID int unsigned not null,
    ALUNO_ID int unsigned not null,
    PONTUACAO decimal not null default 0,
    constraint FK_RANKING_GAMIFICACAO_TURMA
        foreign key (TURMA_ID) references TURMA(ID),
    constraint FK_RANKING_GAMIFICACAO_ALUNO
        foreign key (ALUNO_ID) references ALUNO(ID),
    constraint RANKING_GAMIFICACAO_UNIQUE unique (TURMA_ID, ALUNO_ID)
);