from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse


class HomeView(View):
    def get(self, request):
        return render(request=request, template_name="index.html")


class LogIn(View):
    def get(self, request):
        return render(request=request, template_name="login.html")

    def post(self, request):
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        my_user = authenticate(username=user_name, password=password)
        if my_user is None:
            return HttpResponse('Log in unsuccessfully. The account does not exist')
        login(request, my_user)
        return render(request=request, template_name="login.html")


class Register(View):
    def get(self, request):
        return render(request=request, template_name="register.html")


class VideoPage(View):
    def get(self, request):
        return render(request=request, template_name="video-detail.html")


class VideoPage2(View):
    def get(self, request):
        return render(request=request, template_name="video-detail01.html")

class VideoPage5(View):
    def get(self, request):
        return render(request=request, template_name="video-detail05.html")
class VideoPagePython(View):
    def get(self, request):
        return render(request=request, template_name="video-detail04.html")
class Post1(View):
    def get(self, request):
        return render(request=request, template_name="post1.html")

class Post2(View):
    def get(self, request):
        return render(request=request, template_name="post2.html")

class Post3(View):
    def get(self, request):
        return render(request=request, template_name="post3.html")
class Video6(View):
    def get(self, request):
        return render(request=request, template_name="video-mysql.html")
@decorators.login_required(login_url='/login/')
def view_something(request):
    return HttpResponse("Typically, individuals learning programming exhibit different preferences. "
                        "Some prefer reading documentation, especially when"
                        " they already have a solid knowledge base and can understand "
                        "without detailed explanations or spending time watching videos")


