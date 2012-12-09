from shopcart.checkout import checkout_process


def get_checkout_url(request):
    return checkout_process.get_checkout_url(request)
