from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *

# Create your views here.

def reg(request):
    return render(request, 'my_auth/register.html')


@login_required(login_url=reverse_lazy("log"))
def profile(request):
    return render(request, 'my_auth/profile.html')

def login_view(request):
    redirect_url = reverse("prof")
    if request.method=="GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'my_auth/login.html')

    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        userauth = authenticate(request, username=username, password=password)
        if userauth is not None:
            if userauth.is_active:
                login(request, userauth)
                return profile(request)
        else:
            return render(request, 'my_auth/login.html', {"error":"Пользователь не найден"})
        
def logout_view(request):
    logout(request)
    return redirect(reverse("log"))

# class RegisterUser(CreateView):
#     form_class = RegisterUserForm
#     template_name = 'my_auth/register.html'
#     success_url = reverse_lazy('prof')
    
 
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Регистрация")
    #     return dict(list(context.items()) + list(c_def.items()))


def regist(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            data = {"form" : form}
            return profile(request)
        return render(request, 'my_auth/register.html', data)
    else:
        form = RegisterUserForm()
    data = {"form" : form}
    return render(request, 'my_auth/register.html', data)





