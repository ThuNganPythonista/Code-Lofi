from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self,request):
        return render(request=request,template_name="index.html")

class LogIn(View):
    def get(self,request):
        return render(request=request,template_name="login.html")

class Register(View):
    def get(self,request):
        return render(request=request,template_name="register.html")

class VideoPage(View):
    def get(self,request):
        return render(request=request,template_name="video-detail.html")

class VideoPage2(View):
    def get(self,request):
        return render(request=request,template_name="video-detail01.html")