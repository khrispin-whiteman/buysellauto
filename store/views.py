from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from store.models import Category, Product, Location, EventType


def index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(active=True)
    location = Location.objects.all()
    event_types = EventType.objects.all()

    keywords = request.GET.get('q')
    getcat = request.POST.get('p')

    if category_slug:
        # category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category__slug=category_slug)
        category = category_slug

    if keywords:
        products = products.filter(
            Q(title__icontains=keywords) | Q(user__username__icontains=keywords))

    # if request.user.is_authenticated:
    #     try:
    #         cart = Cart.objects.get(cart_owner=request.user)
    #         cart_items_num = cart.cartitems_set.count()
    #     except:
    #         cart_items_num = 0

    context = {
        #'cart_items_num': cart_items_num,
        'category_slug': category,
        'categories': categories,
        'products': products,
        'keywords': keywords,
        'location': location,
        'event_types': event_types,
    }
    return render(request, 'store/index.html', context)


def product_detail(request, i_d, slug):
    global cart_items_num
    product = get_object_or_404(Product, id=i_d, slug=slug, active=True)
    categories = Category.objects.all()
    images = product.productimage_set.all()

    # if request.user.is_authenticated:
    #     try:
    #         cart = Cart.objects.get(cart_owner=request.user)
    #         cart_items_num = cart.cartitems_set.count()
    #     except:
    #         cart_items_num = 0

    context = {
        'product': product,
        'images': images,
        #'cart_items_num': cart_items_num,
        'categories': categories
    }
    return render(request, 'store/car_detail.html', context)


def product_search(request, category_slug=None):
    global cart_items_num
    cart_items_num = 0
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(active=True)

    keywords = request.GET.get('q')
    getcat = request.POST.get('p')

    if category_slug:
        # category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category__slug=category_slug)
        category = category_slug

    #search
    if keywords:
        products = products.filter(
            Q(title__icontains=keywords) | Q(user__username__icontains=keywords))

    # if request.user.is_authenticated:
    #     try:
    #         cart = Cart.objects.get(cart_owner=request.user)
    #         cart_items_num = cart.cartitems_set.count()
    #     except:
    #         cart_items_num = 0

    context = {
        #'cart_items_num': cart_items_num,
        'category_slug': category,
        'categories': categories,
        'products': products,
        'keywords': keywords,
    }
    return render(request, 'store/search_view.html', context)


def search_filters_brand(request, brand, keywords):
    global cart_items_num
    cart_items_num = 0
    category = None
    #products = Product.objects.filter(active=True)
    categories = Category.objects.all()

    #search
    # if brand:
    #     products = products.filter(
    #         Q(title__icontains=keywords) | Q(user__username__icontains=keywords) | Q(brand__icontains=brand))

    if brand:
        products = Product.objects.filter(
            Q(title__icontains=keywords) | Q(user__username__icontains=keywords) and Q(brand__icontains=brand))

    # if request.user.is_authenticated:
    #     try:
    #         cart = Cart.objects.get(cart_owner=request.user)
    #         cart_items_num = cart.cartitems_set.count()
    #     except:
    #         cart_items_num = 0

    context = {
        #'cart_items_num': cart_items_num,
        'category_slug': category,
        'categories': categories,
        'products': products,
        'keywords': keywords,
    }
    return render(request, 'store/search_view.html', context)