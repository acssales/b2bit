# Mini Twitter (Back-End)

Este sistema foi desenvolvido como parte do desafio do processo seletivo para a B2BIT.

## Descrição geral

Implementar uma API REST em que um usuário possa realizar um cadastro, publicar Posts e ver as publicações de outros usuários.
Utilizar, preferencialmente, Django REST Framework, e banco de dados preferencialmente PostgreSQL.
## Requisitos

### Requisitos obrigatórios (Casos de Uso)

1. [REALIZADO] Caso de Uso 1: Cadastro de usuário
2. [REALIZADO] Caso de Uso 2: Login
3. [REALIZADO] Caso de Uso 3: Publicação de Tweet
4. [REALIZADO] Caso de Uso 4: Feed Geral (10 tweets mais recentes)
5. [REALIZADO] Caso de Uso 5: Feed Personalizado
Obs: No feed, um usuário não deverá ver os próprios tweets

CASO 1: Cadastro de usuário

	O ator faz o cadastro no sistema através da API. Como usuário, ele deve poder fazer o cadastro, para que ele tenha acesso ao Login. Use os campos que achar necessário para a definição do modelo do usuário.


CASO 2: Autenticação (Login)

	O ator deve ser autenticado no sistema através de um Token. Como usuário, ele deve poder fazer login, para que ele tenha acesso ao sistema. Este token deve ter uma data de expiração.


CASO 3: Fazer uma publicação

	O ator cria um post. Esta publicação é persistida no sistema. Como usuário, ele deve poder criar uma publicação, para que possa ser vista por outros usuários do sistema.


CASO 4: Feed geral

    O ator deve receber, no formato JSON, o feed dos últimos 10 posts.


CASO 5: Feed personalizado

    Como usuário, ele deve ter um feed com apenas as publicações de usuários selecionados, para que ele possa ter mais controle do seu feed.
    Este caso de uso é semelhante a uma funcionalidade de feed de pessoas que você segue.

### Requisitos extras
* Deploy
* Diagrama entidade relacional do banco de dados utilizado no projeto
* Testes automatizados
* Deploy do projeto (colocar em produção)
* Upload de arquivos estáticos
* Servir arquivos estáticos. Preferencialmente por uma CDN. Indicamos o AWS S3
* [REALIZADO] Utilizar banco de dados PostgreSQL

### Itens Bonus (não solicitados)
* Logout
* Controle de prazo (semelhante a SCRUM). Ver em: https://docs.google.com/spreadsheets/d/1ZX-whGO1GHcfIXg0e_f0SX-F4tacGiGRgmj4L2YbIGI/edit?usp=sharing

## Tabela de versões dos recursos utilizados

       Recurso        | Versão
----------------------|----------
Python                | 3.8.10
Django                | 4.0.1
Django REST framework | 3.13.1
Tokens(JWT)           | pyJWT-2.3.0
CORS                  | django-cors-headers-3.11.0
Conexão Postgres      | psycopg2-binary-2.9.3
postman (para testes) | (v9/stable) 9.8.3