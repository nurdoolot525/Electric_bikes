from django.urls import path
from .views import home, catalog, product_detail


urlpatterns = [
    path('', home, name='home'),
    path('catalog/', catalog, name='catalog'),
    path('catalog/<int:pk>/', product_detail, name='product_detail'),
]