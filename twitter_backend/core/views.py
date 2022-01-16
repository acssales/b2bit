from rest_framework import viewsets, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import TweetSerializer, UserSerializer
from .models import Tweet, User
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
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
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
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Não autenticado!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Não autenticado!')

        user = User.objects.get(pk=payload['id'])
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
    user = serializers.PrimaryKeyRelatedField(
        # set it to read_only as we're handling the writing part ourselves
        read_only=True,
    )

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        token = self.request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Não autenticado!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Não autenticado!')

        author = User.objects.get(pk=payload['id'])
        serializer.save(user=author)