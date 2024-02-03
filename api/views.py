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
from .serializers import items_srlz,items_srlz_mngr,category_srlz,POST_items_srlz,user_srlz


@api_view(["GET"])
def fisrt_page(rqst):
    usr = rqst.user
    css = """<style>h1{text-align: center;} body {display: flex;justify-content: center;align-items: center;</style>"""
    return HttpResponse(f"<h1>hello_{usr}</h1>{css}",status=200)   

#!================| Helper_func |========================
def mngr_test(rqst,dt): #helper_fucntion
    if rqst.user.groups.filter(name = "manager").exists():
        sz = items_srlz_mngr(dt,many=True)
    else:
        sz = items_srlz(dt,many=True)
    return sz

def is_mngr(rqst):
    if rqst.user.groups.filter(name = "manager").exists():
       return 1
    return 0   
 
def is_dlvr_c(rqst):
    if rqst.user.groups.filter(name = "Delivery_crew").exists():
       return 1
    return 0
#?====================| Searche |=========================
    
def srch(rqst,name=None,prc=None,min_prc=None,max_prc=None,dt=None):
    if dt:
        if name:
            dt = dt.filter(name__contains=name)
        if prc:
            try:
                int(prc)
                dt = dt.filter(price=prc)
            except:
                pass
        elif min_prc or max_prc:
            try:
                int(min_prc)
                dt = dt.filter(price__gte=min_prc)
            except:
                pass
            try:
                int(max_prc)
                dt = dt.filter(price__lte=max_prc)
            except:
                pass
            
            
        return dt



#!=====================================================

@api_view(["GET","POST","PUT","DELETE"])
def menu_items(rqst,inp=None):
    ord_var = rqst.query_params.get("ord") # ordring by
    name    = rqst.query_params.get("name")
    prc     = rqst.query_params.get("prc")
    min_prc = rqst.query_params.get("min_prc")
    max_prc = rqst.query_params.get("max_prc")
    
    if inp:
        try:
            inp = int(inp)
        except:
            return Response({"msg":"bad request"},400)

    if (rqst.method == "GET"):
        
        if (inp == None): #All_items
            if rqst.user.groups.filter(name = "manager").exists():
                dt = item.objects.all()
            else:
                dt = item.objects.filter(is_actv=1)
            
            dt = srch(rqst,name,prc,min_prc,max_prc,dt)
            if ord_var:
                try:
                    ord_filds = ord_var.split(",")
                    dt_ord = dt.order_by(*ord_filds)
                    dt = dt_ord
                except:
                    pass
                
            sz = mngr_test(rqst,dt)  
            return Response({"items":sz.data},200)
        
        else: #singel item
            dt = item.objects.filter(id = inp)    
            sz = mngr_test(rqst,dt)

            return Response({"item":sz.data},200)
    
    if (rqst.method == "POST"):
        if is_mngr():
            dt = rqst.data
            sz = POST_items_srlz(data = dt)

            if sz.is_valid():
                item.objects.create(**dt)
                return Response({"msg":"Created"},201)
            return Response({"msg":"bad request"},400)
        
        return Response({"msg":"you cant do this process"},403)
    
    if (rqst.method == "PUT"): #update
        if is_mngr(rqst) :
            if inp:
                dt = rqst.data

                sz = POST_items_srlz(data = dt)
                if sz.is_valid():

                    item.objects.filter(id = inp).update(**dt)
                    return Response({"msg":"update"},201)
            return Response({"msg":"bad request"},400)
        
        return Response({"msg":"you cant do this process"},403)
    
    if (rqst.method == "DELETE"): #update
        if is_mngr(rqst):
            if inp:
                item.objects.filter(id = inp).delete()
                return Response({"msg":"deleted"},201)
            
            return Response({"msg":"bad request"},400)
        
        return Response({"msg":"you cant do this process"},403)
    
