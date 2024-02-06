from django.contrib import admin
from .models import item,category,order

admin.site.register(item)
admin.site.register(category)
# admin.site.register(cart)
admin.site.register(order)