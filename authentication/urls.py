from django.urls import path
from .views import homeconex, register,logIn

urlpatterns = [
   
    path('',homeconex, name="connexions" ),
    path('register',register, name="enregistrer"),
    path('login', logIn, name="login")
]
