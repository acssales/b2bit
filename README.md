# Mini Twitter (Back-End)

Por Augusto Cezar Souza Sales (augustcezar@gmail.com)

Este sistema foi desenvolvido como parte do desafio do processo seletivo para a B2BIT.

## Descrição geral

Implementar uma API REST em que um usuário possa realizar um cadastro, publicar Posts e ver as publicações de outros usuários.
Utilizar, preferencialmente, Django REST Framework, e banco de dados preferencialmente PostgreSQL.
## Requisitos

### Requisitos obrigatórios (Casos de Uso)

1. [REALIZADO] Cadastro de usuário
2. [REALIZADO] Login
3. [REALIZADO] Publicação de Tweet
4. [REALIZADO] Feed Geral (10 tweets mais recentes)
5. [REALIZADO] Feed Personalizado
Obs: No feed, um usuário não deverá ver os próprios tweets

CASO 1: Cadastro de usuário

> O ator faz o cadastro no sistema através da API. Como usuário, ele deve poder fazer o cadastro, para que ele tenha acesso ao Login. Use os campos que achar necessário para a definição do modelo do usuário.


CASO 2: Autenticação (Login)

> O ator deve ser autenticado no sistema através de um Token. Como usuário, ele deve poder fazer login, para que ele tenha acesso ao sistema. Este token deve ter uma data de expiração.


CASO 3: Fazer uma publicação

> O ator cria um post. Esta publicação é persistida no sistema. Como usuário, ele deve poder criar uma publicação, para que possa ser vista por outros usuários do sistema.


CASO 4: Feed geral

> O ator deve receber, no formato JSON, o feed dos últimos 10 posts.


CASO 5: Feed personalizado

> Como usuário, ele deve ter um feed com apenas as publicações de usuários selecionados, para que ele possa ter mais controle do seu feed.
Este caso de uso é semelhante a uma funcionalidade de feed de pessoas que você segue.

### Requisitos extras

* [ ] Diagrama entidade relacional do banco de dados utilizado no projeto
* [ ] Testes automatizados
* [X] Deploy do projeto (colocar em produção) [^2]
* [ ] Upload de arquivos estáticos
* [ ] Servir arquivos estáticos. Preferencialmente por uma CDN. Indicamos o AWS S3
* [x] Utilizar banco de dados PostgreSQL [^1]

### Itens Bonus (não solicitados)

* [X] Logout
* [X] Acesso via ferramenta externa (Postman)
* [X] Controle de prazo (semelhante a SCRUM). Ver em: https://docs.google.com/spreadsheets/d/1ZX-whGO1GHcfIXg0e_f0SX-F4tacGiGRgmj4L2YbIGI/edit?usp=sharing
* [X] Ver seu perfil (todos os dados exceto a senha)
* [X] Senha "encriptada" armazenada via hash
* [X] Regra de negócio adicional: Um usuário não pode seguir a si mesmo
* [X] Regra de negócio adicional: Um usuário não pode seguir outro várias vezes (a relação é única a cada momento)

## Tabela de versões dos recursos utilizados

|          Recurso            |           Versão           |
|-----------------------------|----------------------------|
|Python                       | 3.8.10                     |
|Django                       | 4.0.1                      |
|Django REST framework        | 3.13.1                     |
|Tokens(JWT)                  | pyJWT-2.3.0                |
|CORS                         | django-cors-headers-3.11.0 |
|Conexão Postgres             | psycopg2-binary-2.9.3      |
|postman (para testes)        | (v9/stable) 9.8.3          |
|python-decouple (para deploy)| 3.5                        |
|django-heroku (para deploy)  | 0.3.1                      |

[^1]: Foi utilizado também o sqlite3 durante parte do desenvolvimento, antes da mudança para um psql local e finalmente, o psql utilizado no deploy.
[^2]: Utilizei o Heroku pois minha conta na AWS está inativa. No entanto, sei utilizar a EC2 também.

# Forma de utilização

1. Criação de usuário
- Vá para: https://b2bit.herokuapp.com/api/register/
- Envie um JSON via POST no formato:
```
{
    "nickname": "Seu Nome",
    "atname": "@seu_nome",
    "bio": "Sua descrição",
    "email": "seu_email@provedor.com",
    "password": "sua senha"
}
```
-------------------

2. Login
- Vá para: https://b2bit.herokuapp.com/api/login/
- Envie um JSON via POST no formato:
```
{
    "atname": "@seu_nome",
    "password": "sua senha"
}
```
-------------------

3. Ver seu perfil
- Vá para: https://b2bit.herokuapp.com/api/user/
- Envie um GET sem parametros

-------------------

4. Logout
- Vá para: https://b2bit.herokuapp.com/api/logout/
- Envie um POST sem parâmetros

-------------------

5. Tuitar
- Vá para: https://b2bit.herokuapp.com/api/user/tweet/
- Envie um JSON via POST no formato:
```
{
    "tweet_text": "texto do seu tweet."
}
```
5.1. Ver todos os tweets
- Vá para: https://b2bit.herokuapp.com/api/user/tweet/
- Envie um GET sem parametros
- Esta função foi deixada intencionalmente para facilitar os testes de uso

-------------------

6. Seguir outro usuario
- Vá para: https://b2bit.herokuapp.com/api/user/follow/
- Envie um JSON via POST no formato:
```
{
    "following_user": "user_id"
}
```

-------------------

7. Ver o feed geral (10 tweets, exceto os seus)
- Vá para: https://b2bit.herokuapp.com/api/user/feed_geral/
- Envie um GET sem parametros

-------------------

8. Ver o feed personalizado (10 tweets, somente de quem você segue)
- Vá para: https://b2bit.herokuapp.com/api/user/feed_selecionado/
- Envie um GET sem parametros
