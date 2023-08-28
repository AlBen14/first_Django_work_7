from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Advertisment
from .forms import AdvertsForm
from django.core.exceptions import ValidationError
from django.db.models import Count
from django.contrib.auth import get_user_model
# from django.http import HttpResponse

# Create your views here.
User=get_user_model()

def index(request):
    title=request.GET.get("qwery")
    if title:
        adverts=Advertisment.objects.filter(title__icontains=title)
    else:
        adverts=Advertisment.objects.all()
    context={"advert":adverts, "title":title}
    return render(request, 'my_adverts/index.html', context)

def topSellers(request):
    users = User.objects.annotate(adv_count=Count("advertisment")).order_by("-adv_count")
    context = {"users":users}
    return render(request, 'my_adverts/top-sellers.html', context)

def advertisement_post(request):
    if request.method=="POST":
        form = AdvertsForm(request.POST ,request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            if title[0] == "?":
                raise ValidationError('Нельзя добавить логин со знаком вопроса')
            advertisment = Advertisment(**form.cleaned_data)
            advertisment.user = request.user
            advertisment.save()
            url = reverse('main_page')
        return redirect(url)
    else:
        form = AdvertsForm()
    context = {"form" : form}
    return render(request, 'my_adverts/advertisement-post.html',context)

def advert__details(request,pk):
    advert = Advertisment.objects.get(id=pk)
    context={"advert":advert,}
    return render(request, 'my_adverts/advertisement.html',context)

# def register(request):
#     return render(request, 'my_adverts/register.html')

# def login(request):
#     return render(request, 'my_adverts/login.html')

# def profile(request):
#     return render(request, 'my_adverts/profile.html')

