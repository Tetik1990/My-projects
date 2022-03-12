from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('team/', Players.as_view(), name='team'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('team/<str:slug>/', GetPlayer.as_view(), name='player'),
    path('search/', Search.as_view(), name='search'),

]
