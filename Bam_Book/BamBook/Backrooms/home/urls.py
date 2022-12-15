from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path("", views.home, name="home"),
     path("index/", views.login, name="login"),
     path("index_logined/", views.logout_auth, name="logout")
]