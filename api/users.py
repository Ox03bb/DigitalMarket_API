from django.http                import HttpResponse,JsonResponse
from rest_framework.response    import Response
from rest_framework.views       import APIView
from rest_framework.decorators  import api_view
from rest_framework             import status
from django.contrib.auth.models import User

from rest_framework.permissions    import IsAuthenticated
from rest_framework.decorators      import authentication_classes,permission_classes,throttle_classes


from . import views
from .models import item,category,cart,order
from .serializers import user_srlz,mngr_srlz

from rest_framework.authtoken.models import Token

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
        
    if "last_name" in rqst.data:
        usr_oldt.first_name = rqst.data["last_name"]

#!================|For mngr_only |==========================
    if "email" in rqst.data:

        if mngr:

            if User.objects.filter(email = rqst.data["email"]):

                return Response({"msg":"exists email"},400)
                 
            usr_oldt.email = rqst.data["email"]
        else:
            return Response({"msg":"you cant do this process"},403)

    if "is_superuser" in rqst.data:
        if mngr:
            usr_oldt.is_superuser = rqst.data["is_superuser"]
        return Response({"msg":"you cant do this process"},403)
    
    if "is_staff" in rqst.data:
        if mngr:
            usr_oldt.is_staff = rqst.data["is_staff"]
        return Response({"msg":"you cant do this process"},403)
    
    if "is_active" in rqst.data:
        if mngr:
            usr_oldt.is_active = rqst.data["is_active"]
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


    
@api_view(["GET","PUT","DELETE"])
def users(rqst,inp=None):
    
    if rqst.method == "GET": 
        if rqst.user.groups.filter(name = "manager").exists():
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
            return Response({"msg":"you cant do this process"},403)

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

@api_view(["GET","POST","PUT","DELETE"])
def me(rqst):
    if rqst.method == "GET":
        usr = rqst.user.id
        dt = User.objects.filter(id=usr)
        sz = user_srlz(dt,many=True)
        return Response({"me":sz.data},200)
    
    