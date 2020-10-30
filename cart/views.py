from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def shopping_cart(request):
    """shows shopping cart page """
    return render(request, 'cart/shopping_cart.html')


def add_item_to_cart(request, item_id):

    """Addeds the Item to bag  """

    quantity = int(request.POST.get('quantity'))
    active_url = request.POST.get('active_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(active_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('shopping_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping bag"""

    try:

        cart = request.session.get('cart', {})

        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
