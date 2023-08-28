from django.urls import path
from .views import *

urlpatterns = [
        path("register",regist , name="reg"),
        path("login", login_view , name="log"),
        path("profile", profile , name="prof"),
	path("logout", logout_view , name="logout"),
]