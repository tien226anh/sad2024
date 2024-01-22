from django.urls import path, include
from .views import show_cart

urlpatterns = [
    path(
        "",
        view=show_cart,
        name="show_cart",
    ),
]
