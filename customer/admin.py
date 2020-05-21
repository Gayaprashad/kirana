from django.contrib import admin
from .models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=('userName',)
    list_display_links=('userName',)
    search_fields=('userName','adl1','adl2','phno','locality','city')
    list_per_page=25


admin.site.register(Customer, CustomerAdmin)