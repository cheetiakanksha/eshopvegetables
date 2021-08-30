from django.core import paginator
from django.shortcuts import render,redirect
from .models import order, products
from django.core.paginator import Paginator
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(request):

    product_objects = products.objects.all()
    template_name = 'shop/index.html'
    # Search funtionality
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:                             #For querysets questions please view the page
        product_objects =product_objects.filter(title__icontains = item_name) #https://sodocumentation.net/django/topic/1235/querysets

    #Paginator code & link 
    #https://docs.djangoproject.com/en/3.2/topics/pagination/
    paginator = Paginator(product_objects,4)
    page_number = request.GET.get('page')
    product_objects = paginator.get_page(page_number)

    return render(request,template_name,{'product_objects': product_objects})


def detail(request,obj_id):
    product_objects = products.objects.get(id=obj_id)
    return render(request,'shop/detail.html',{'product_objects':product_objects})

def checkout(request):

    if request.method == 'POST':

        items =request.POST.get('items',"") #allow the null value thats why put the empty string ""
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total','')
        order_list = order( items = items,name = name, email = email, address = address, city = city, state = state, zipcode = zipcode,total = total)
        order_list.save();

    return render(request,'shop/checkout.html')
def login(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        email=request.POST['email']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('login')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                print('email taken')
                return redirect('login')
            else:

                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save();
            return redirect('register')
    else:
        messages.info(request,'passwords should match')
    return render(request,'shop/login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credintials')
            return redirect('register')    

    else:

         return render(request,'shop/register.html')   
def logout(request):
    auth.logout(request)
    return redirect('/') 
def payment(request):
    if request.method=='POST':
        owner=request.POST['owner']
        cvv=request.POST['cvv']
        cardnumber=request.POST['cardnumber']
        
              
    return render(request,'shop/payment.html')
def final(request):
    return render(request,'shop/final.html')    


