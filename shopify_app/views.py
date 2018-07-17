import shopify
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render
# from django.core.urlresolvers import reverse
from django.urls import reverse
import hashlib, base64, hmac, json
from django.conf import settings
from django.http import HttpResponseForbidden
import urllib, re


def _return_address(request):
    return request.session.get('return_to') or reverse('root_path')


def login(request):
    # Ask user for their ${shop}.myshopify.com address

    # If the ${shop}.myshopify.com address is already provided in the URL,
    # just skip to authenticate
    if request.GET.get('shop') or request.POST.get('shop'):
        return authenticate(request)
    context = {}
    return render(request, 'shopify_app/login.html', context)


def _hmac_is_valid(request):
    params = urllib.parse.parse_qsl(request.META.get('QUERY_STRING'))
    cleaned_params = []
    hmac_value = request.GET.get('hmac')

    # Sort parameters
    for (k, v) in sorted(params):
        if k in ['hmac', 'signature']:
            continue
        cleaned_params.append((k, v))

    new_qs = urllib.parse.urlencode(cleaned_params, safe=":/")
    secret = settings.SHOPIFY_API_SECRET.encode("utf8")
    h = hmac.new(secret, msg=new_qs.encode("utf8"), digestmod=hashlib.sha256)

    # Compare digests
    return hmac.compare_digest(h.hexdigest(), hmac_value)


def authenticate(request):
    '''
    see: https://help.shopify.com/en/api/getting-started/authentication/oauth for details of all authentication tasks
    to perform
    :param request:
    :return:
    '''
    if not _hmac_is_valid(request):
        return HttpResponseForbidden()

    shop = request.GET.get('shop') or request.POST.get('shop')
    if shop:
        regex = '[a-zA-Z,0-9.\-]+myshopify.com'
        if re.match(regex, shop):
            scope = settings.SHOPIFY_API_SCOPE
            redirect_uri = request.build_absolute_uri(reverse('shopify_app.views.finalize'))
            permission_url = shopify.Session(shop.strip()).create_permission_url(scope, redirect_uri)
            return redirect(permission_url)
        else:
            return HttpResponseForbidden()

    return redirect(_return_address(request))


def finalize(request):
    shop_url = request.GET.get('shop')
    try:
        shopify_session = shopify.Session(shop_url)
        request.session['shopify'] = {
            "shop_url": shop_url,
            "access_token": shopify_session.request_token(request.REQUEST)
        }

    except Exception:
        messages.error(request, "Could not log in to Shopify store.")
        return redirect(reverse('shopify_app.views.login'))

    messages.info(request, "Logged in to shopify store.")

    response = redirect(_return_address(request))
    request.session.pop('return_to', None)
    return response


def logout(request):
    request.session.pop('shopify', None)
    messages.info(request, "Successfully logged out.")

    return redirect(reverse('shopify_app.views.login'))
