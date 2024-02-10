from django.urls import path,include
from . import menu_items,users,cart,order
from rest_framework.authtoken.views import Token
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items/',menu_items.menu_items),
    path('menu-items/<str:inp>',menu_items.menu_items ),

    path('users/',users.users ),
    path('users/me',users.me ),
    path('users/<str:inp>',users.users),
    
    path('login',users.login),
    path('logout',users.logout ),
    
    path('groups/manager/users',users.all_mngr),
    path('groups/manager/users/<str:inp>',users.all_mngr),
    path('groups/delivery-crew/users',users.all_dely ),
    path('groups/delivery-crew/users/<str:inp>',users.all_dely ),

    path('orders',order.ord_fncs),
    path('orders/<str:inp>',order.ord_fncs),

]