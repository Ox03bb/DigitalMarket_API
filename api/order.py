from rest_framework.response    import Response

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication

from .models import item,itme_in_cart,cart,order,ord_itm
from .serializers import cart_item_srlz,items_srlz,ord_srlz,ord_itm_srlz




@permission_classes([IsAuthenticated])   
@api_view(["GET","POST","PUT","DELETE"])
def ord_fncs(rqst,inp=None):
    
    if rqst.method == "GET":  
        if rqst.user.groups.filter(name = "manager").exists() or rqst.user.groups.filter(name = "Delivery_crew").exists():
            if inp :
                allord = order.objects.filter(id=inp)
                sz_all = ord_srlz(allord,many=True)
            else:    
                allord = order.objects.all()
                sz_all = ord_srlz(allord,many=True)
            
            return Response({"all_orders":sz_all.data},200)         
            
        else:
            allord = order.objects.filter(user_id=rqst.user.id)
            sz_all = ord_srlz(allord,many=True)
            
            return Response({"my_orders":sz_all.data},200)    
        
    if rqst.method == "POST": 
        cid = cart.objects.get(user_id_id=rqst.user.id)
        cart_itm = itme_in_cart.objects.filter(cart_id_id=cid.id)
        
        sz = cart_item_srlz(cart_itm,many=True)
        ord_id = order.objects.create(user_id_id=rqst.user.id)
        cnt = 0
            
        try:
            while 1:
                ord_itm.objects.create(cnt=sz.data[cnt]["itm_cnt"],itm_id_id=sz.data[cnt]["itm_id_id"],ord_id_id=ord_id.id)
                cnt += 1
                
        except:
            itm_arr = []
            cnt_arr = []
            cnt = 0
            Citm = itme_in_cart.objects.filter(cart_id_id=cid)
            print(Citm[cnt].itm_cnt)
            try:
                while 1:
                    itm_arr.append(int(Citm[cnt].itm_id_id))
                    cnt_arr.append(int(Citm[cnt].itm_cnt))
                    cnt += 1

            except:
                cnt=0
                for i in itm_arr:
                    itm = item.objects.get(id = int(i))
                    new_cnt =  int(itm.cnt)
                    new_cnt -= cnt_arr[cnt]
                    if new_cnt == 0:
                        # itm.update(cnt= 0,is_actv=0)
                        itm.cnt = 0
                        itm.is_actv =0
                        itm.save()
                    elif new_cnt > 0:
                        # itm.update(cnt= new_cnt)
                        print(new_cnt)
                        itm.cnt = new_cnt
                        itm.save()

                    cnt += 1
             
                Citm.delete()
                return Response(200) 