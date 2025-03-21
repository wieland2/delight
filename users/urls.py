from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser, name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('settings/', views.userSettings, name="settings"),
    path('<str:username>/', views.profile, name="profile")
]
