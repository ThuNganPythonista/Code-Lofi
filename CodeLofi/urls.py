from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', HomeView.as_view(),name="home"),
    path('login/', LogIn.as_view(), name="login"),
    path('register/', Register.as_view(), name="register"),
    path('video/', VideoPage.as_view(), name="video"),
    path('video-css/', VideoPage.as_view(), name="video-css"),
]
