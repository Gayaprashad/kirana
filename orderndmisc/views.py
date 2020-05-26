from django.shortcuts import render,redirect
from retailer.models import Items
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
from django.contrib.auth.models import User
from .models import Temporder,Order
from django .contrib import messages

# Create your views here.

def item(request):
    items = Items.objects.all()

    paginator =Paginator(items,2)
    page= request.GET.get('page')
    paged_items =paginator.get_page(page)

    context ={
        'items' : paged_items
    }

    return render( request,'itemndcart/item.html',context)

# It adds the items to the temporary order DB

def addcart(request):

    if request.method == 'POST':
        item_id = request.POST['id']
        quantity = request.POST['quantity']
        if request.user.is_authenticated:
            user = request.user
        items = Items.objects.filter(id=item_id)
        for i in items:
            print(i)
         
        temp_order= Temporder(user=user, item=i, item_id= item_id, quantity=quantity)
        temp_order.save()
        return redirect('cart')
    else:
        messages.error(request,'The method is not POST')
        return redirect('cart')
    return

# It displays the cart page

def cart(request):

    # To display the data in Temporder table

    if request.user.is_authenticated:
        user = request.user
        items = Temporder.objects.filter(user=user)
        k=0
        sum =[]
        for item in items:
            sum.append(item.item.price* item.quantity)
            k +=1
        
        Total_sum=0
        for s in sum:
            Total_sum +=s
        context ={
            'itemsL' : items,
            'sum'   : Total_sum
        }
        return render(request,'itemndcart/cart.html',context)
    else:
        messages.error(request,'The user is not logged in')
        return redirect('login')
    return

def remcart(request,item_id):

    if(request.user.is_authenticated):
        user = request.user
    else:
        messages.error(request,'The user is not logged in')
        return redirect('login')
    item = Temporder.objects.filter(item_id=item_id).filter(user=user).delete()
    return redirect('cart')

def order(request):

    items = Temporder.objects.all()

    for item in items:
        cur_order= Order(user = item.user, item = item.item, items_id =item.items_id,username = item.user.username, quantity= item.quantity)
        cur_order.save()
    
    Temporder.objects.all().delete()
    
    return redirect('index')

def emptyuser(request):
    messages.error(request,'First Login before placing an order')
    return render(request,'customer/login.html')