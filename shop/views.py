from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse

from .models import Product, User


def index(request):
    user = User.objects.get(id=1)
    product_list = Product.objects.all()
    template = loader.get_template('shop/index.html')
    context = {
        'product_list': product_list,
        'username': user.username
    }
    return HttpResponse(template.render(context, request))

def add_to_cart(request, product_id):
    user = User.objects.get(id=1)
    user.cart = str(product_id) + "," + str(user.cart)
    user.save()

    return HttpResponseRedirect(reverse('shop:index'))

def add(request, product_id):
    user = User.objects.get(id=1)
    user.cart = str(product_id) + "," + str(user.cart)
    user.save()
    return HttpResponseRedirect(reverse('shop:cart'))

def remove(request, product_id):
    user = User.objects.get(id=1)
    user.cart = str(user.cart).replace(str(product_id) + ",", "", 1)
    user.save()
    return HttpResponseRedirect(reverse('shop:cart'))

def cart(request):
    user = User.objects.get(id=1)
    # not use first element
    product_amt = [-1, 0, 0, 0, 0]
    products = str(user.cart).split(',')
    while '' in products:
        products.remove('')

    for x in products:
        product_amt[int(x)] += 1

    print(product_amt)

    product_list = []
    if products:
        product_list = Product.objects.filter(id__in=products)
        for x in product_list:
            product = Product.objects.get(id=x.id)
            product.amt = product_amt[x.id]
            print(product.amt)
            product.save()

        product_list = Product.objects.filter(id__in=products)

    template = loader.get_template('shop/cart.html')
    context = {
        'product_list': product_list,
        'username': user.username
    }
    return HttpResponse(template.render(context, request))
