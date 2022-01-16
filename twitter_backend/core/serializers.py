from rest_framework import serializers
from .models import User, Tweet


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
        model=Tweet
        fields = ['id', 'user', 'tweet_text', 'likes', 'pub_date']