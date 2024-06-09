from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name =  'home'),
    path('register/',views.user_register, name =  'register'),
    path('login/',views.user_login, name =  'login'),
    path('logout/',views.user_logout, name =  'logout'),
    path('profile/',views.user_profile, name =  'profile'),
    path('pass_change/',views.user_passwordChange, name =  'pass_change'),
    path('pass_change2/',views.user_passwordChange2, name =  'pass_change2'),
]
