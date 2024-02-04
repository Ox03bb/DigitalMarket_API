from django.urls import path,include
from . import views,users
from rest_framework.authtoken.views import Token
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items/',views.menu_items),
    path('menu-items/<str:inp>',views.menu_items ),

    path('users/',users.users ),
    path('users/me',users.me ),
    path('users/<str:inp>',users.users),
    path('users/login',obtain_auth_token ),
    path('users/logout',users.me ),
]