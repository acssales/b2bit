from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class User(AbstractUser):
    nickname = models.CharField(max_length=30)   # Apelido que aparece como nome nas publicacoes
    atname = models.CharField(max_length=30, unique=True, null=False)   # O @ do usuario
    bio = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'atname'
    REQUIRED_FIELDS = []


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   # Autor do tweet
    tweet_text = models.CharField(max_length=280)    # Sim, desde 2017 os tweets passaram de 140 para 280 caracteres...
    likes = models.IntegerField(default=0)           # Quantidade de "coracoes" recebidos
    pub_date = models.DateField(default=now)  # Data de publicacao