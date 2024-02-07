from django.http                import HttpResponse,JsonResponse
from rest_framework.response    import Response
from rest_framework.views       import APIView
from rest_framework             import status
from django.contrib.auth.models import User,Group
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication


from .models import item,itme_in_cart,cart
from .serializers import cart_item_srlz,items_srlz

from rest_framework.authtoken.models import Token


@permission_classes([IsAuthenticated])   
@api_view(["GET","POST","PUT","DELETE"])
def cart_fncs(rqst):
      
    if IsAuthenticated().has_permission(rqst,None):
        cid = cart.objects.get(user_id_id = rqst.user.id)
    else:
        return Response({"msg":"U have to Authenticate"},401)

    if rqst.method == "GET":        
        itm_in_c = itme_in_cart.objects.filter(cart_id_id = cid.id)
        if not itm_in_c:
            return Response({"msg":"Empty cart"},200)

        sz       = cart_item_srlz(itm_in_c,many=True)
        itm_ids = []
        itm_cnt = []
        i = 0
        try:
            while i > -1:
                dt = dict(sz.data[i])
                itm_ids.append(dt["itm_id_id"])
                itm_cnt.append(dt["itm_cnt"])
                i += 1
        except:
            out_itm = []
            cnt = 0
            prc = 0
            for i in itm_ids:
                itm = item.objects.get(id=i)
                itm.cnt = itm_cnt[cnt]
                prc += itm.cnt*itm.price
                sz = items_srlz(itm)
                out_itm.append(sz.data)
                cnt += 1
            out_itm.append({"total price" : f"{prc}"})
            return Response(out_itm,200)

    if rqst.method == "POST":
        try:#data validation
            int(rqst.data["id"])
            int(rqst.data["cnt"])
        except:
            return Response({"msg":"bad rqst"},400)
            
        try:
            itm =  item.objects.get(id=rqst.data["id"])
            if int(rqst.data["cnt"]) > int(itm.cnt):
                return Response({"msg":"the cnt u rqst is grater then what is avaliable"},400)
            try:
                iic = itme_in_cart.objects.get(cart_id_id=cid.id,itm_id_id=rqst.data["id"])
                iic.itm_cnt += int(rqst.data["cnt"])
                iic.save()
                return Response({"msg":"added to cart"},200)
            except:
                
                itme_in_cart.objects.create(cart_id_id=cid.id, itm_id_id=rqst.data["id"], itm_cnt=rqst.data["cnt"])          
            
            return Response({"msg":"added to cart "},200)

        except:       
            return Response({"msg":"item does not exist"},400)
    
    if rqst.method == "PUT":
       
        if rqst.data["id"] and rqst.data["cnt"]:
            try:#data validation
                int(rqst.data["id"])
                int(rqst.data["cnt"])
            except:
                return Response({"msg":"bad rqst"},400)
           
            try: 
                itm = item.objects.get(id = rqst.data["id"])
                if int(itm.cnt) <  int(rqst.data["cnt"]):
                    return Response({"msg":"the cnt u rqst is grater then what is avaliable"},400)
                else:

                    if int(rqst.data["cnt"]) == 0:
                        itm = itme_in_cart.objects.get(cart_id_id=cid.id,itm_id_id=rqst.data["id"]).delete()
                        return Response({"msg":"Updated"},200)
                    elif int(rqst.data["cnt"]) > 0:
                        itm = itme_in_cart.objects.get(cart_id_id=cid.id,itm_id_id=rqst.data["id"])
                        itm.itm_cnt =  rqst.data["cnt"]
                        itm.save()
                        return Response({"msg":"Updated"},200)
                    else:
                        return Response({"msg":"bad rqst"},400)
            except:
                return Response({"msg":"item does not exist in your cart"},400)
           
        elif rqst.data["id"] :
            try:#data validation
                int(rqst.data["id"])
            except:
                return Response({"msg":"bad rqst"},400)
            try:
                itm = itme_in_cart.objects.get(cart_id_id=cid.id,itm_id_id=rqst.data["id"]).delete()
                return Response({"msg":"cart cleaned"},200)

            except:
                return Response({"msg":"item does not exist in your cart"},400)
        
        else:
            return Response({"msg":"Bad rqst"},400)
        
    if rqst.method == "DELETE":
        try:
            itm = itme_in_cart.objects.get(cart_id_id=cid.id).delete()
            return Response({"msg":"item was deleted"},200)     
        except:
            return Response({"msg":"item not found"},400)