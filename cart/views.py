from django.shortcuts import render
from cart import cart


# Create your views here.
def show_cart(request, template_name="cart/cart.html"):
    if request.method == "POST":
        postdata = request.POST.copy()
        if postdata["submit"] == "Remove":
            cart.remove_from_cart(request)
        if postdata["submit"] == "Update":
            cart.update_cart(request)
    cart_item_count = cart.cart_item_count(request)
    cart_items = cart.get_cart_items(request)
    page_title = "Shopping Cart"
    cart_subtotal = cart.cart_subtotal(request)
    return render(
        request,
        template_name,
        locals(),
    )
