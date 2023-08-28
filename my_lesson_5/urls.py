from django.urls import path
from .views import *

urlpatterns = [
	path("",index , name="main_page"),
    path("top-seller", topSellers , name="top-sellers"),
    path("advertisement-post", advertisement_post , name="advertisement-post"),
    path("advert/<int:pk>", advert__details, name="adv-detail")
    # path("register",register , name="register"),
    # path("login", login , name="login"),
    # path("profile", profile , name="profile"),
]

