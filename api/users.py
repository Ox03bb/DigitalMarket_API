from rest_framework.response    import Response

from django.contrib.auth.models import User,Group
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes,throttle_classes

from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from .throttling import Five_by_h
from rest_framework.authtoken.views import ObtainAuthToken

from .models import item,category,order,cart
from .serializers import user_srlz,mngr_srlz,POST_user_srlz

from rest_framework.authtoken.models import Token

import re

#?================|updater Function |===================

def updater(rqst,inp):
    usr_oldt = User.objects.get(id=inp)
    mngr = rqst.user.groups.filter(name = "manager").exists()

#================|For anyone |==========================
    if "username" in rqst.data :

        if User.objects.filter(username=rqst.data["username"]):
            return Response({"msg":"exists user name"},400)
        usr_oldt.username = rqst.data["username"]
        
    if "first_name" in rqst.data:
        usr_oldt.first_name = rqst.data["first_name"]  
    
    if "password" in rqst.data:
        if chek_pass(rqst,usr_oldt) :
            rqst.data["password"]  = make_password(rqst.data["password"] )
        else:    
            return Response({"msg":"Bad password"},400)

    if "last_name" in rqst.data:
        usr_oldt.first_name = rqst.data["last_name"]
    
    if "last_name" in rqst.data:
        usr_oldt.first_name = rqst.data["last_name"]

#!================|For mngr_only |==========================
    if mngr:
        if "email" in rqst.data:
                if User.objects.filter(email = rqst.data["email"]):
                   return Response({"msg":"exists email"},400)
                if chek_email(rqst):
                    usr_oldt.email = rqst.data["email"]
                else:
                    return Response({"msg":"email Not valid"},400)
        if "groups" in rqst.data :
            # - for delet gfrom group || split for add in many groups one time
            grp = Group.objects.filter(id__in=rqst.data["groups"])
            usr_oldt.groups.set(grp)
            
        if "is_superuser" in rqst.data:
                usr_oldt.is_superuser = rqst.data["is_superuser"]

        if "is_staff" in rqst.data:
                usr_oldt.is_staff = rqst.data["is_staff"]

        if "is_active" in rqst.data:
                usr_oldt.is_active = rqst.data["is_active"]
    else:
        if "email" in rqst.data or "is_superuser" in rqst.data or "is_staff" in rqst.data or "is_active" in rqst.data:
            return Response({"msg":"you cant do this process"},403)
#!===============================================================

    if mngr:
        sz = mngr_srlz(usr_oldt)
    else:
        sz = user_srlz(usr_oldt)

    if sz.is_valid:
        usr_oldt.save()
        return Response({"msg":"updated"},200)
    else:
        return Response({"msg":"bad request"},400)

#?===============================================================
#?==================|check_Email Function |======================
def chek_email(rqst):
    email =rqst.data["email"]
    ptt  = "^[a-zA-Z0-9. _-]+@[a-zA-Z0-9. -]+\. [a-zA-Z]{2,4}$"
    if re.search(pattern=ptt,string=email) :
        return 1
    return 0
#?=================|check_password Function |====================

def chek_pass(rqst,usr_oldt=None):
    first_tst = 0
    pss =rqst.data["password"]
    ln = len(pss)
    ptt ="(?=.*[0-9]?)(?=.*[a-z])(?=.*[A-Z])(?=.*\W?)(?!.* ).{8,32}"
    #at least : Aa
    
    if  ln < 8 or ln >= 32:
        return 0
    
    if rqst.method == "POST":
        if rqst.data["username"] :
            if pss == rqst.data["username"]:
                return 0
        if rqst.data["email"] :
            if pss == rqst.data["email"]:
                return 0
        if rqst.data["first_name"] :
            if pss == rqst.data["first_name"]:
                return 0
        if rqst.data["last_name"] :
            if pss == rqst.data["last_name"]:
                return 0
        first_tst = 1    
        
    elif rqst.method == "PUT" and usr_oldt:
        
        if pss == usr_oldt.username:
            return 0
        if pss == usr_oldt.email:
            return 0
        if pss == usr_oldt.first_name:
            return 0
        if pss == usr_oldt.last_name:
            return 0
        
        first_tst = 1 
        
    if re.search(pattern=ptt,string=pss) and first_tst == 1 :
        return 1
    
    return 0
#?===============================================================


@permission_classes([AllowAny])   
@api_view(["GET","POST","PUT","DELETE"])
def users(rqst,inp=None):
    
    if rqst.method == "GET": 
        if rqst.user.groups.filter(name="manager").exists():
            if inp:
                try:
                    inp = int(inp)
                except:
                    return Response({"msg":"bad request"},400)
                usr = User.objects.filter(id=inp)
                sz = mngr_srlz(usr,many=True)
                return Response({"user":sz.data},200)
            else:
                usr = User.objects.all()
                sz = mngr_srlz(usr,many=True)
                return Response({"users":sz.data},200)
        else:
            return Response({"users_func_GET":"you cant do this process"},403)

    if rqst.method == "POST": #Create New_User 
        
        dt = rqst.data
        pss = rqst.data["password"]

        if chek_pass(rqst):
            rqst.data["password"] = make_password(pss)
            dt = rqst.data
            sz = POST_user_srlz(data = dt)
            if sz.is_valid():
                
                user = User.objects.create(**sz.data)
                cart.objects.create(user_id_id= user.id)
                
                return Response({"user":"Created"},200)
            print(sz.data)
            return Response({"user":"bad request"},400)
        return Response({"user":"unvalid password"},400)
    
    if rqst.method == "PUT": 
        if rqst.user.groups.filter(name = "manager").exists():  
            
            if inp:
                return updater(rqst,inp)          
        return Response({"msg":"you cant do this process"},403)
    
    if rqst.method == "DELETE": 
        if rqst.user.groups.filter(name = "manager").exists():  
            try:
                usr = User.objects.get(id=inp)
            except:
                return Response({"msg":"user not found"},400)
            if usr:
                usr.delete()
                return Response({"Deleted"},200)
            else:
                return Response({"msg":"bad request"},400)


@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])   
@api_view(["GET","PUT","DELETE"])
def me(rqst):
    if rqst.method == "GET":
        usr = rqst.user.id
        dt = User.objects.filter(id=usr)
        sz = user_srlz(dt,many=True)
        return Response({"me":sz.data},200)
    
    if rqst.method == "PUT":
        usr = rqst.user.id
        return updater(rqst,usr)
    
    if rqst.method == "DELETE":
        usr_id = rqst.user.id
        usr = User.objects.get(id=usr_id)
        usr.is_active = 0
        usr.save()
        return Response({"msg":"disactivated"},200)

#?======================-| groups/manager |-===========================
@api_view(["GET","POST","DELETE"])
def all_mngr(rqst,inp=None):
    
    if rqst.user.groups.filter(name = "manager").exists():
        if rqst.method == "GET":
                usr = User.objects.filter(groups__name='manager')
                sz = mngr_srlz(usr,many=True)
                return Response({"managers":sz.data},200)

        if rqst.method == "POST":
            uid = int(rqst.data["id"])
            if uid >= 0:  #For add user from mngr group
                grp = Group.objects.filter(name="manager")
                user = User.objects.get(id = rqst.data["id"])
                user.groups.set(grp)
                return Response({"msg":"user upgraded"},200)
            else: #For delet user from mngr group
                grp = Group.objects.get(name="manager")
                uid = int(rqst.data["id"])
                user = User.objects.get(id = -uid )
                user.groups.remove(int(grp.id))
                return Response({"msg":"user degraded"},200)
        
        if rqst.method == "DELETE":
            grp = Group.objects.get(name="Delivery_crew")
            user = User.objects.get(id = inp)
            user.groups.remove(int(grp.id))
            return Response({"msg":"user degraded"},200)
        
    return Response({"msg":"Forbiden"},403)

@api_view(["GET","POST","DELETE"])
def all_dely(rqst,inp=None):
    
    if rqst.user.groups.filter(name = "manager").exists():
        if rqst.method == "GET":
                usr = User.objects.filter(groups__name='Delivery_crew')
                sz = mngr_srlz(usr,many=True)
                return Response({"Delivery_crew":sz.data},200)

        if rqst.method == "POST":
            uid = int(rqst.data["id"])
            if uid >= 0:  #For add user from mngr group
                grp = Group.objects.filter(name="Delivery_crew")
                user = User.objects.get(id = rqst.data["id"])
                user.groups.set(grp)
                return Response({"msg":"user upgraded"},200)
            else: #For delet user from mngr group
                grp = Group.objects.get(name="Delivery_crew")
                uid = int(rqst.data["id"])
                user = User.objects.get(id = -uid )
                user.groups.remove(int(grp.id))
                return Response({"msg":"user degraded"},200)

        if rqst.method == "DELETE":
            grp = Group.objects.get(name="Delivery_crew")
            user = User.objects.get(id = inp )
            user.groups.remove(int(grp.id))
            return Response({"msg":"user degraded"},200)
    
    return Response({"msg":"Forbiden"},403)

#?======================-==================-===========================

#!======================-| Auth |-===========================
from rest_framework.authtoken.views import ObtainAuthToken


@api_view(["POST"])
@throttle_classes([Five_by_h])
def login(rqst):
    
    if rqst.method == "POST":
        if not rqst.user.is_authenticated:
            return ObtainAuthToken.as_view()(rqst._request)
        else:
            return Response({"msg":"u are alredy auth"},403) 

@permission_classes([IsAuthenticated])   
@api_view(["POST"])
def logout(rqst):
    
    if rqst.method == "POST":
        
        try:
            tkn = Token.objects.get(user_id=rqst.user.id)
            tkn.delete()
            return Response({"msg":"Logout done"},200)

        except:
            return Response({"logout":"Error"},400)
    return Response({"msg":"Error"},400)
    