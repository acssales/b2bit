from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from rest_framework.exceptions import AuthenticationFailed
import jwt

class CurrentUser(models.Manager):
    def get_current_user(self, request):
        """Retorna o usuário logado responsável pelo request"""
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Não autenticado!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Não autenticado!')

        user = User.objects.get(pk=payload['id'])

        return user

class User(AbstractUser):
    nickname = models.CharField(max_length=30)   # Apelido que aparece como nome nas publicacoes
    atname = models.CharField(max_length=30, unique=True, null=False)   # O @ do usuario
    bio = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    objects = CurrentUser() # Acrescenta o metodo get_current_user ao 'objects'

    USERNAME_FIELD = 'atname'
    REQUIRED_FIELDS = []


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   # Autor do tweet
    tweet_text = models.CharField(max_length=280)    # Sim, desde 2017 os tweets passaram de 140 para 280 caracteres...
    likes = models.IntegerField(default=0)           # Quantidade de "coracoes" recebidos
    pub_date = models.DateTimeField(default=now)  # Data de publicacao