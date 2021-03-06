from django.shortcuts import render, redirect, reverse
# Create your views here.


def view_cart(request):
    ''' for viewing whats in the cart '''

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a merchandise to cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """ update to cart """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        del cart[item_id]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_item(request, item_id):
    """ Delete a item from the cart """
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        del cart[item_id]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
