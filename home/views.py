import shopify
from django.shortcuts import render
from django.conf import settings

from shopify_app.decorators import shop_login_required


def welcome(request):
    context = {
        'callback_url': "http://%s/login/finalize" % (request.get_host()),
    }
    return render(request, 'home/welcome.html', context)


@shop_login_required
def index(request):
    products = shopify.Product.find(limit=3)
    orders = shopify.Order.find(limit=3, order="created_at DESC")
    context = {
        'products': products,
        'orders': orders,
        'SHOPIFY_API_KEY': settings.SHOPIFY_API_KEY,
    }
    return render(request, 'home/index.html', context)


def design(request):
    return render(request, 'home/design.html', {})
