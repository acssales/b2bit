from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView
from .views import TweetViewSet, GeneralFeedViewSet

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),

    path('user/tweet/', TweetViewSet.as_view({'post': 'create', 'get': 'list'})),
    path('user/feed_geral/', GeneralFeedViewSet.as_view({'get': 'list'}))
]
