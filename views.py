from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order
from math import ceil

# Create your views here.


def index(request):
    print('popat66', request)
    # return HttpResponse("Index Shop")
    products = Product.objects.all()
    print('gop11', products)
    # print("type aksh is", type(products))
    # n = len(products)
    # print(n)
    # nslides = n//4 + ceil((n/4) - (n//4))
    # params = {'no_of_slides':nslides, 'product':products, 'range1':range(1, nslides)}
    # allprods = [[products, range(1,nslides), nslides],[products, range(1, nslides), nslides] ]
    import random
    # lis = ['danger', 'warning', 'info', 'primary', 'dark']

    allprods = []
    catprods = Product.objects.values('category', 'id')
    print("kru", catprods)
    cats = {item['category'] for item in catprods}
    print("kru1", cats)
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        print("gopi", prod)
        # print("ru12", prod)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        import random
        # lis = ['danger', 'warning', 'info', 'primary']
        # ran = random.choice(lis)
        # lis.remove(ran)
        # if len(lis) == 0:
        #     lis = ['danger', 'warning', 'info', 'primary', 'dark']
        allprods.append([prod, range(1, nslides), nslides])
    # print('cataksh', cats)
    params = {'allprods1': allprods}
    # print("paramsaksh", params['allprods1'])
    return render(request, 'app22/index.html', params)

def searchMatch(query, item):
    if query in item.desc.lower() or query in item.product_name.lower():
        return True


def search(request):
    query = request.GET.get('search')
    # return HttpResponse("we are at search")

    allprods = []
    catprods = Product.objects.values('category', 'id')
    print("kru", catprods)
    cats = {item['category'] for item in catprods}
    print("kru1", cats)
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allprods.append([prod, range(1, nslides), nslides])

    params = {'allprods1': allprods}

    return render(request, 'app22/index.html', params)
    # return render(request, 'app22/search.html')


def about(request):
    # return HttpResponse("we are at about")
    return render(request, 'app22/about.html')


def contact(request):
    thank = False
    if request.method == "POST":
        print(request)
        name9 = request.POST.get('name8', '')
        email9 = request.POST.get('email8', '')
        phone9 = request.POST.get('phone8', '')
        message9 = request.POST.get('message8', '')
        print(name9, email9, message9)
        thank = 10
        contact1 = Contact(name=name9, email=email9,
                           desc=message9, phone=phone9)
        contact1.save()

    # a = Contact.objects.all()
    # for i in a:
    #     print('aary6',i,  i.product_id )
    # print('rudra993', a)

    # return HttpResponse("we are at contact")
    return render(request, 'app22/contact.html', {'thank': thank})


def tracker(request):
    # return HttpResponse("we are at tracker")
    return render(request, 'app22/tracker.html')


def productview(request, myid):
    # return HttpResponse("we are at prodview")
    producta = Product.objects.filter(id=myid)
    # print("disha", product)
    return render(request, 'app22/prodview.html', {'product99': producta[0]})


def checkout(request):
    # return HttpResponse("we are at checkout")
    if request.method == "POST":
        itemsJson = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + \
            request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        thank = 10
        # id = Order.order_id
        a = Order.objects.all()
        id = a[len(a)-1]
        order = Order(name=name, email=email, address=address,
                      city=city, state=state, zip=zip_code, phone=phone, items_json=itemsJson)
        order.save()
        # thank = True
        return render(request, 'app22/checkout.html', {'thank': thank, 'id': id})
    thank = False
    return render(request, 'app22/checkout.html', {'thank': thank})
