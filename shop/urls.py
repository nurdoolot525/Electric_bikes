from django.urls import path
from .views import (home, catalog, product_detail, cart, add_to_cart,
                    remove_from_cart, increase_quantity, decrease_quantity, clear_cart, checkout)


urlpatterns = [
    path('', home, name='home'),
    path('catalog/', catalog, name='catalog'),
    path('catalog/<int:pk>/', product_detail, name='product_detail'),
    path('cart/', cart, name='cart'),
    path('cart/add/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>/', remove_from_cart, name='remove_from_cart'),
    path('cart/plus/<int:pk>/', increase_quantity, name='increase_quantity'),
    path('cart/minus/<int:pk>/', decrease_quantity, name='decrease_quantity'),
    path('cart/clear/', clear_cart, name='clear_cart'),
    path('checkout/', checkout, name='checkout'),
]