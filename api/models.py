from django.db import models
from django.contrib.auth.models import User



#============ Items ===============

class item(models.Model):
    name       = models.CharField(max_length=254)
    discription= models.CharField(max_length=254,null=True)
    cnt        = models.IntegerField(null=True)
    price      = models.DecimalField(max_digits=8,decimal_places=2)
    is_avlb    = models.BooleanField(default=1)
    is_actv    = models.BooleanField(default=1)
    catigoty   = models.ManyToManyField("category", through="itm_ctgr")


class itm_ctgr(models.Model):
    item_id     = models.ForeignKey(item, on_delete=models.CASCADE)
    category_id = models.ForeignKey("category", on_delete=models.CASCADE)

#============ category ===============    
class category(models.Model):
    name  = models.CharField(max_length=254)
    
    def __str__(self) -> str:
        return self.name

#============ order ===============

class order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    price   = models.DecimalField(max_digits=8,decimal_places=2)
    date    = models.DateField()
    is_deliverd = models.BooleanField()
    catigoty= models.ManyToManyField(item, through="ord_itm")

class ord_itm(models.Model):
    itm_id = models.ForeignKey(item, on_delete=models.PROTECT)
    ord_id = models.ForeignKey(order, on_delete=models.PROTECT)
    cnt    = models.IntegerField()


# #============ Cart ===============
class cart(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE) #OneToOneField make teh coulmn uniq


class itme_in_cart(models.Model):
    cart_id = models.ForeignKey(cart, on_delete=models.CASCADE)
    itm_id  = models.ForeignKey(item, on_delete=models.CASCADE)
    itm_cnt = models.IntegerField()
    