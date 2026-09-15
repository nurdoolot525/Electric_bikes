from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product, WinterBike, Equipment, Review
import random

CHAR_FIELDS = [
    ('Цвет', 'color'),
    ('Год', 'year'),
    ('Диаметр колеса', 'wheel_size'),
    ('Материал рамы', 'frame_material'),
    ('Размер', 'size'),
    ('Страна', 'country'),
    ('Производитель', 'manufacturer'),
    ('Покрышки', 'tires'),
    ('Рама', 'frame'),
    ('Подседельный штырь', 'seatpost'),
    ('Седло', 'saddle'),
    ('Вилка', 'fork'),
    ('Вынос', 'stem'),
    ('Колеса', 'wheels'),
    ('Руль', 'handlebar'),
    ('Тип тормозов', 'brake_type'),
    ('Тормозная система', 'brake_system'),
    ('Манетки', 'shifters'),
    ('Система шатунов', 'crankset'),
    ('Задний переключатель', 'rear_derailleur'),
    ('Цепь', 'chain'),
    ('Количество скоростей', 'speeds'),
    ('Гарантия', 'warranty'),
]

def get_characteristics(product):
    result = []
    for label, field in CHAR_FIELDS:
        value = getattr(product, field, '')
        if value:
            result.append((label, value))
    return result

def home(request):
    products = Product.objects.all()
    winter_bikes = WinterBike.objects.all()
    equipment = Equipment.objects.all()
    reviews = Review.objects.all()
    return render(request, 'home.html', {'products': products, 'winter_bikes': winter_bikes, 'equipment': equipment, 'reviews': reviews})


def catalog(request):
    products = Product.objects.all()

    if request.GET.get('in_stock'):
        products = products.filter(is_available=True)

    min_price = request.GET.get('min_price')
    if min_price:
        products = products.filter(price__gte=min_price)

    max_price = request.GET.get('max_price')
    if max_price:
        products = products.filter(price__lte=max_price)

    brand = request.GET.get('brand')
    if brand:
        products = products.filter(title__istartswith=brand)

    sort = request.GET.get('sort', 'new')
    if sort == 'cheap':
        products = products.order_by('price')
    elif sort == 'expensive':
        products = products.order_by('-price')
    else:
        products = products.order_by('-id') 

    brand_counts = {}
    for product in Product.objects.all():
        name = product.title.split()[0]
        brand_counts[name] = brand_counts.get(name, 0) + 1
    brands = sorted(brand_counts.items())

    paginator = Paginator(products, 5)
    page_obj = paginator.get_page(request.GET.get('page'))

    for product in page_obj:
        chars = get_characteristics(product)
        random.shuffle(chars)
        product.card_characteristics = chars[:3]

    params = request.GET.copy()
    if 'page' in params:
        params.pop('page')
    query_params = params.urlencode()

    return render(request, 'catalog.html', {
        'page_obj': page_obj,
        'brands': brands,
        'selected_brand': brand or '',
        'min_price': min_price or '',
        'max_price': max_price or '',
        'in_stock': bool(request.GET.get('in_stock')),
        'sort': sort,
        'query_params': query_params,
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    similar_products = Product.objects.exclude(pk=pk)[:4]

    sizes = [s.strip() for s in product.sizes.split(',') if s.strip()]
    colors = [c.strip() for c in product.colors.split(',') if c.strip()]

    characteristics = get_characteristics(product)

    return render(request, 'detail.html', {
        'product': product,
        'similar_products': similar_products,
        'sizes': sizes,
        'colors': colors,
        'characteristics': characteristics,
    })


# Create your views here.
