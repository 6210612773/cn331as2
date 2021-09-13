from django.urls import path
from . import views

app_name='users'
urlpatterns = [
    
    path('', views.indexPage, name="index"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutPage, name="logout"),



]