from rest_framework.response    import Response

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication

from .models import item,itme_in_cart,cart,order,ord_itm
from .serializers import cart_item_srlz,items_srlz,ord_srlz,ord_itm_srlz




@permission_classes([IsAuthenticated])   
@api_view(["GET","POST","PUT","DELETE"])
def ord_fncs(rqst):
    
    if rqst.method == "GET":  
        if rqst.user.groups.filter(name = "manager").exists():
            allord = order.objects.all()
            orditm = ord_itm.objects.all()
            
            sz_all = ord_srlz(allord,many=True)
            print(allord)
            print(sz_all.data)
            i = 0
            # try:
            #     dt = sz_all.data
            #     print("====================")
            #     print(allord)
            #     while i > -1:
            #         print(dt[i])
            #         i += 1
            # except:
            return Response(200)         
            
            