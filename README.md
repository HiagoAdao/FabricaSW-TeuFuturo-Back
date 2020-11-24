# #TeuFuturo

Projeto backend da matéria  _Fábrica de Software_  na disciplina  _Desafios da Tecnologia e Inovação_  do curso de _Ciência da Computação_ na faculdade [IMED](https://www.imed.edu.br/).

A API pode ser encontrada neste [link](https://teu-futuro-backend.herokuapp.com).

---
<!-- PRINCIPAIS-TECNOLOGIAS -->
## Principais tecnologias utilizadas
As principais tecnologias utilizadas foram:
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Marshmallow](https://marshmallow.readthedocs.io/)
- [PyJWT](https://pyjwt.readthedocs.io/)
- [Peewee](http://docs.peewee-orm.com/)
- [Flake8](https://flake8.pycqa.org/en/latest/)
- [MySQL](https://www.mysql.com/)
- [Docker](https://docs.docker.com/compose/)
- [Gunicorn](http://docs.gunicorn.org/_/downloads/en/19.x/pdf/)
- [Heroku](https://www.heroku.com/)

<!-- REQUERIMENTOS -->
## Requerimentos

É necessário fazer a instalação do projeto antes do rodar localmente, para isso execute os passos abaixo na raiz do projeto:

- Criar um ambiente virtual ([venv](https://docs.python.org/3/library/venv.html)) para a instalação, executando o seguinte comando:
```sh
python3 -m venv {nome da sua venv}
```
- Ativar o ambiente virtual (LINUX e MAC)
```bash
source venv/bin/activate
```
- Ativar o ambiente virtual (WINDOWS)
```bash
venv/bin/activate.bat
```
- Instalar as dependências
```sh
make install
```
- Ter o [Docker](https://docs.docker.com/compose/) instalado e rodando, e inicializar o banco de dados:
```
make db-start
```

Todos os comandos completos podem ser encontrados no arquivo `Makefile` na raiz do projeto.

<!-- EXECUCAO -->
## Execução

Para a execução do projeto local, utilize o comando abaixo:
```sh
make start
```

<!-- DEPLOYMENT -->
## Deployment
Todo **_commit_** ou **_pull request_** feito na branch `master` irá gerar um deploy automático pelo serviço do - [Heroku](https://www.heroku.com/) que pode ser econtrado na url do projeto de produção.


<!-- CONTACT -->
## Contact

- [Hiago Adão Müller Oliveira](https://www.linkedin.com/in/hiago-adão-müller-oliveira-b223b1161)

- [Isaura Koch](https://www.linkedin.com/in/isaura-koch-a3a990169/)
