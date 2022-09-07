from django.shortcuts import render
from .models import Product,Contact,Orders
from math import ceil

from django.http import HttpResponse
from django.views.generic import ListView
from .models import Product
from django.http import JsonResponse
import json



# Create your views here.
from django.http import HttpResponse

def json(request):
    data = list(Product.objects.values())
    return JsonResponse(data,safe=False)

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        phone=request.POST.get('phone','')
        email=request.POST.get('email','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)


    return render(request, 'shop/prodView.html', {'product':product[0]})

def checkout(request):
    if request.method=="POST":
        item_json = request.POST.get('itemsJson', '')
        name=request.POST.get('name','')
        phone=request.POST.get('phone','')
        email=request.POST.get('email','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        address=request.POST.get('address1','') +" " +request.POST.get('address2','')
        order=Orders(item_json=item_json,name=name,email=email,phone=phone,address=address,city=city,state=state,zip_code=zip_code)
        order.save()
        thank=True
        id=order.order_id
        return render(request, 'shop/checkout.html',{'thank':thank,'id':id})
    return render(request, 'shop/checkout.html')