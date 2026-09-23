from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, WinterBike, Equipment, Review, Question
import random


def price_text(number):
    return f'{number:,}'.replace(',', ' ') + ' ₽'

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


def cart(request):
    cart_ids = request.session.get('cart', [])

    cart_items = []
    total = 0
    for product in Product.objects.filter(id__in=cart_ids):
        quantity = cart_ids.count(product.id)
        total = total + product.price * quantity

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'price': price_text(product.price),
            'old_price': price_text(product.old_price) if product.old_price else '',
        })

    order = {
        'number': '789563678',
        'sum': price_text(total),
        'discount': price_text(0),
        'total': price_text(total),
    }

    similar_products = list(Product.objects.all()[:3])

    for product in similar_products:
        product.price_text = price_text(product.price)
        product.old_price_text = price_text(product.old_price) if product.old_price else ''

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'order': order,
        'similar_products': similar_products,
    })


def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if product.is_available:
        cart_ids = request.session.get('cart', [])
        cart_ids.append(product.id)
        request.session['cart'] = cart_ids

    next_page = request.GET.get('next', 'cart')
    return redirect(next_page)


def remove_from_cart(request, pk):
    cart_ids = request.session.get('cart', [])
    cart_ids = [item for item in cart_ids if item != pk]
    request.session['cart'] = cart_ids

    return redirect('cart')


def increase_quantity(request, pk):
    cart_ids = request.session.get('cart', [])
    cart_ids.append(pk)
    request.session['cart'] = cart_ids

    return redirect('cart')


def decrease_quantity(request, pk):
    cart_ids = request.session.get('cart', [])
    if pk in cart_ids:
        cart_ids.remove(pk)
    request.session['cart'] = cart_ids

    return redirect('cart')


def clear_cart(request):
    request.session['cart'] = []

    return redirect('cart')


def checkout(request):
    cart_ids = request.session.get('cart', [])

    total = 0
    for product in Product.objects.filter(id__in=cart_ids):
        total = total + product.price * cart_ids.count(product.id)

    data = {
        'name': request.POST.get('name', ''),
        'surname': request.POST.get('surname', ''),
        'city': request.POST.get('city', ''),
        'street': request.POST.get('street', ''),
        'house': request.POST.get('house', ''),
        'flat': request.POST.get('flat', ''),
        'phone': request.POST.get('phone', ''),
        'email': request.POST.get('email', ''),
        'comment': request.POST.get('comment', ''),
        'delivery': request.POST.get('delivery', 'courier'),
        'payment': request.POST.get('payment', 'online'),
    }

    if data['city']:
        data['address'] = data['city'] + ', ул. ' + data['street'] + ', д. ' + data['house'] + ', кв. ' + data['flat']
    else:
        data['address'] = ''

    return render(request, 'checkout.html', {
        'data': data,
        'order_count': len(cart_ids),
        'order_sum': price_text(total),
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


def contacts(request):
    if request.method == 'POST':
        Question.objects.create(
            name=request.POST.get('name', ''),
            email=request.POST.get('email', ''),
            phone=request.POST.get('phone', ''),
            company=request.POST.get('company', ''),
            message=request.POST.get('message', ''),
        )
    return render(request, 'contacts.html')


# Create your views here.
