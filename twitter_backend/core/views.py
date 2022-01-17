from rest_framework import viewsets, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import FollowingSerializer, TweetSerializer, UserSerializer
from .models import Tweet, User, Following
import jwt
import datetime


class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):

    def post(self, request):
        atname = request.data['atname']
        password = request.data['password']

        user = User.objects.filter(atname=atname).first()

        if user is None:
            raise AuthenticationFailed('Usuário não encontrado!')

        if not user.check_password(password):
            raise AuthenticationFailed('Senha Incorreta!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=180),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response


class UserView(APIView):

    def get(self, request):
        user = User.objects.get_current_user(request)
        serializer = UserSerializer(user)

        return Response(serializer.data)


class LogoutView(APIView):

    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'sucesso'
        }
        return response


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    user = UserSerializer(many=True, read_only=True)

    def perform_create(self, serializer):
        # Identifica o autor do tweet automaticamente
        author = User.objects.get_current_user(self.request)
        serializer.save(user=author)

class FollowingViewSet(viewsets.ModelViewSet):
    serializer_class = FollowingSerializer

    def perform_create(self, serializer):
        # Identifica o autor do tweet automaticamente
        follower = User.objects.get_current_user(self.request)
        serializer.save(user=follower)


class GeneralFeedViewSet(viewsets.ViewSet):

    def list(self, request):
        # 10 tweets mais recentes
        # Regra de negocio: o autor não vê os próprios tweets no feed
        feed = Tweet.objects.exclude(user=User.objects.get_current_user(request)).order_by('-pub_date')[:10]
        serializer = TweetSerializer(feed, many=True)
        return Response(serializer.data)


class SelectedFeedViewSet(viewsets.ViewSet):
    def list(self, request):
        # 10 tweets mais recentes
        # Regra de negocio: o autor não vê os próprios tweets no feed
        following_obj = Following.objects.filter(user=User.objects.get_current_user(request)) # Encontra a lista de usuários seguidos pelo usuário logado
        if following_obj.exists():
            following = [f.following_user for f in following_obj]
            feed = Tweet.objects.filter(user__in=following).order_by('-pub_date')[:10] # Somente funciona se o usuário segue alguém
        else:
            feed = Tweet.objects.none() # Caso o usuário não siga ninguém, retorna uma lista vazia
        serializer = TweetSerializer(feed, many=True)
        return Response(serializer.data)