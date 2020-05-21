from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin (admin.ModelAdmin):
    list_display=('item_id','quantity')
    list_display_links=('item_id',)

admin.site.register(Order, OrderAdmin)