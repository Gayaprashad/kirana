from django.shortcuts import render,redirect
from orderndmisc.models import Order
# Create your views here.

def order_list(request):

    orders = Order.objects.all()

    context ={
        'orders':orders
    }
    return render(request,'retailer/order_list.html',context)

def fulfilled(request,order_id):
    order= Order.objects.filter(id=order_id).delete()
    return redirect('order_list')