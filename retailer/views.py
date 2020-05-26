from django.shortcuts import render,redirect
from orderndmisc.models import Order
from django.contrib.auth.models import User
from customer.models import Customer
# Create your views here.

def order_list(request):

    orders = Order.objects.all()
    
    
    context ={
        'orders':orders
    }

    return render(request,'retailer/order_list.html',context)

def fulfilled(request,order_id):
    if request.method =='POST':
        order_id =request.POST['cust_id']
    befdel_order=Order.objects.filter(id=order_id)

    for o in befdel_order:
       cust_user=o.user

    order= Order.objects.filter(id=order_id).delete()
    
    order_items = Order.objects.filter(user= cust_user)

    temp_customer=Customer.objects.filter(user = cust_user)
    for cust in temp_customer:
        cust_customer=cust
    context={
        'customer': cust_customer,
        'user_customer': cust_user,
        'items': order_items
    }
    if request.method == 'POST':
        return render(request,'retailer/delivery_list.html',context)
    else:
        return redirect('order_list')

def delivery_listings(request):
    # The distinct_customer variable represents the oder object corresponding each and every unique user who has ordered the items
    distinct_customers= Order.objects.order_by('username').distinct('username')
    
    # This class is made to hold the different users,the number of items ordered by then and their localities 
    class Set:
        def __init__(self,user,count,locality):
            self.unique_user= user
            self.count=count
            self.locality= locality

        def order_of_unique_user(self):
            return self.unique_user

        def count(self):
            return self.count
        
        def locality(self):
            return self.locality

    unique_cust =[]
    for unique_cust_order in distinct_customers:
        cust= Customer.objects.filter(user=unique_cust_order.user).get()
        unique_cust.append(cust)
        print (type(cust))
    
    

    # This tries to find out the number of items that is ordered by one unique customer
    item_count=[]
    z=0
    for customer in distinct_customers:
        corresponding_items =Order.objects.filter(username= customer.username)
        item_count.append(int(0))
        for items in corresponding_items:
            item_count[z] += 1
        z+=1
        # print('items')

    localities =[]
    k=0
    customers = Customer.objects.all()
    for corresponding_user in distinct_customers:
        for cust in customers:
            if corresponding_user.user.id == cust.user.id:
                localities.append(cust.locality)
        # print("localities")

    list_mine =[]
    for a,b,c in zip(unique_cust,item_count,localities) :
        custom_set = Set(a,b,c)
        list_mine.append(custom_set)
    
    context={
        'sets':list_mine
    }

    return render(request,'retailer/delivery_listings.html',context)

def delivery_listing(request,cust_id):
    customer = Customer.objects.filter(id=cust_id)
    for cust in customer:
        alt_cust =cust
        user_customer =User.objects.filter(id=cust.user.id)
    orders = Order.objects.filter(user= alt_cust.user)
    
    context={
        'customer': alt_cust,
        'user_customer': user_customer,
        'items': orders
    }
    return render(request,'retailer/delivery_list.html',context)
    # return render(request,'retailer/delivery_list.html')

def user_listings(request):
    cust = Customer.objects.all()
    context ={
        'customers': cust
    }
    return render(request,'retailer/user_list.html',context)

def rem_cust(request,customer_id):
    cust= Customer.objects.filter(id= customer_id)
    for c in cust:
        user= c.user
    cust.delete()
    user.delete()
    return redirect('user_listings')