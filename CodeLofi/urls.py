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
    path('video-python/', VideoPagePython.as_view(), name="video-python"),
    path('video-django/', VideoPage5.as_view(), name="video-django"),
    path('video-css/', VideoPage.as_view(), name="video-css"),
    path('view-product/',view_something, name="view-something")
]
