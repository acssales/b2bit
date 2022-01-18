from django.db import models
from django.db.models import Q, F
from django.contrib.auth.models import AbstractUser
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
    pub_date = models.DateTimeField(auto_now_add=True)     # Data de publicacao
    class Meta:
        ordering = ["-pub_date"]


class Following(models.Model):
    user = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)          # Seguidor
    following_user = models.ForeignKey(User, related_name="followed", on_delete=models.CASCADE) # Usuário sendo seguido
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user','following_user'],  name="unique_followers"), # Só há um registro de cada par (seguidor, seguido)
            models.CheckConstraint(check=~Q(user=F('following_user')), name="cant_follow_yourself") # Um usuário não pode seguir a si mesmo
        ]

    def __str__(self):
        return f"{self.user} follows {self.following_user}"
