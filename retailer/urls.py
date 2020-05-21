from django.urls import path,include
from . import views

urlpatterns=[
    path('order_list',views.order_list,name='order_list'),
    path('fulfilled/<int:order_id>',views.fulfilled,name='fulfilled')
]