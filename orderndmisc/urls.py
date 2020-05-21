from django.urls import path, include
from . import views

urlpatterns =[
    path('item',views.item, name='item'),
    path('addcart',views.addcart,name='addcart'),
    path('remcart/<int:item_id>',views.remcart,name='remcart'),
    path('cart',views.cart, name='cart'),
    path('order',views.order, name='order')
]