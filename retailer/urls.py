from django.urls import path,include
from . import views

urlpatterns=[
    path('order_list',views.order_list,name='order_list'),
    path('fulfilled/<int:order_id>',views.fulfilled,name='fulfilled'),
    path('delivery_listings',views.delivery_listings,name='delivery_listings'),
    path('delivery_listing/<int:cust_id>',views.delivery_listing, name='delivery_listing'),
    path('user_listings',views.user_listings,name="user_listings"),
    path('rem_cust/<int:customer_id>',views.rem_cust,name="rem_cust")
]