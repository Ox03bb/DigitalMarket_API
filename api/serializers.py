from rest_framework import serializers
from .models import item


class category_srlz(serializers.Serializer):
    name = serializers.CharField(max_length = 254)
    
    def __str__(self) -> str:
        return self.name

    
class items_srlz(serializers.ModelSerializer):
    catigoty = serializers.StringRelatedField(many=True)

    class Meta:
        model = item
        fields = ['name', 'cnt', 'price','catigoty']
    
class items_srlz_mngr(serializers.ModelSerializer):
    catigoty = serializers.StringRelatedField(many=True)

    class Meta:
        model = item
        fields = "__all__"
        
class POST_items_srlz(serializers.Serializer):
    name    = serializers.CharField(max_length=254)
    discription= serializers.CharField(max_length=254,default=None)
    cnt     = serializers.IntegerField()
    price   = serializers.DecimalField(max_digits=8,decimal_places=2)
    is_avlb = serializers.BooleanField(default=1)
    is_actv = serializers.BooleanField(default=1)
