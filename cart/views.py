from django.shortcuts import render
from cart import cart


# Create your views here.
def show_cart(request, template_name="cart/cart.html"):
    cart_items = cart.get_cart_items(request)
    page_title = "Shopping Cart"
    cart_subtotal = cart.cart_subtotal(request)
    return render(
        request,
        template_name,
        locals(),
    )
