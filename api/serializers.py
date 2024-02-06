from rest_framework import serializers
from .models import item

from django.contrib.auth.models import User


#!================| Items |======================
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
    name        = serializers.CharField(max_length=254)
    discription = serializers.CharField(max_length=254,default=None)
    cnt         = serializers.IntegerField()
    price       = serializers.DecimalField(max_digits=8,decimal_places=2)
    is_avlb     = serializers.BooleanField(default=1)
    is_actv     = serializers.BooleanField(default=1)

#!================| User |======================
class mngr_srlz(serializers.ModelSerializer):
    groups = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ["id","username","first_name","last_name","email","groups","date_joined","last_login","is_superuser","is_staff","is_active"]
        read_only_fields = ["id","date_joined","last_login"]
        extra_kwargs = {'password': {'write_only': True}}
class user_srlz(serializers.ModelSerializer):
    groups = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ["id","username","password","first_name","last_name","email","groups","date_joined","last_login"]
        read_only_fields = ["id","groups","date_joined","last_login"]
        extra_kwargs = {'password': {'write_only': True}}
class POST_user_srlz(serializers.Serializer):
    username   = serializers.CharField(max_length=150)
    password   = serializers.CharField(max_length=128)
    email      = serializers.CharField(max_length=128)
    first_name = serializers.CharField(max_length=150)
    last_name  = serializers.CharField(max_length=150)

