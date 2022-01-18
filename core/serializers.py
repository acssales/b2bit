from rest_framework import serializers
from .models import Following, User, Tweet


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nickname', 'atname', 'bio', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True} # Evita que a senha seja exposta
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            # Aplica função hash à senha para armazenar de forma segura
            instance.set_password(password)
        instance.save()
        return instance


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'user', 'tweet_text', 'likes', 'pub_date']
        extra_kwargs = {
            # Permite que o front-end veja o dono do tweet, sem precisar informá-lo ao publicar
            'user': {'required': False, 'allow_null': True},
            # Permite que a data não seja informada
            'pub_date': {'required': False, 'allow_null': True}
        }

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = ['id', 'user','following_user']
        extra_kwargs = {
            # Usuário não deve ser informado, será identificado automaticamente
            'user': {'required': False, 'allow_null': True}
        }