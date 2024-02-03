from django.urls import path,include
from . import views,users

urlpatterns = [
    path('menu-items/',views.menu_items),
    path('menu-items/<str:inp>',views.menu_items ),

    path('users/',users.users ),
    path('users/me',users.me ),
    path('users/<str:inp>',users.users),
] 