from itertools import chain

import django
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from aboutus.models import CompanyContactDetails, CompanySocialMediaLinks
from agents.models import Agent
from businessdirectory.models import Equipment, AutoShopAndCarWash
from orders.forms import OrderForm
from store.models import Category, Product, Location, EventType, Event


def index(request, category_slug=None):
    category = None
    # globals
    categories = Category.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    equipments = Equipment.objects.filter(active=True)
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')

    # other
    products = Product.objects.filter(active=True)
    hire_products = Product.objects.filter(active=True, listing_type='For Hire')

    keywords = request.GET.get('q')
    getcat = request.POST.get('p')

    if category_slug:
        # category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category__slug=category_slug)
        category = category_slug

    if keywords:
        products = products.filter(
            Q(title__icontains=keywords) | Q(user__username__icontains=keywords))
        if products.count() == 0:
            products = products.filter(
                Q(title__icontains=keywords) | Q(user__username__icontains=keywords))

    # if request.user.is_authenticated:
    #     try:
    #         cart = Cart.objects.get(cart_owner=request.user)
    #         cart_items_num = cart.cartitems_set.count()
    #     except:
    #         cart_items_num = 0

    context = {
        # 'cart_items_num': cart_items_num,
        'category_slug': category,
        'categories': categories,
        'companycontactdetails': companycontactdetails,
        'companysocialmedialinks': companysocialmedialinks,
        'location': location,
        'event_types': event_types,
        'products': products,
        'equipments': equipments,
        'keywords': keywords,
        'hire_cars': hire_products,
        'all_agents': clearing_agents,
    }
    return render(request, 'store/index.html', context)


def vehicles(request, category_slug=None):
    category = None
    # globals
    categories = Category.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    equipments = Equipment.objects.filter(active=True)
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')

    # other
    products = Product.objects.filter(active=True)
    hire_products = Product.objects.filter(active=True, listing_type='For Hire')

    keywords = request.GET.get('q')
    getcat = request.POST.get('p')

    if category_slug:
        # category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category__slug=category_slug)
        category = category_slug

    if keywords:
        products = products.filter(
            Q(title__icontains=keywords) | Q(user__username__icontains=keywords))
        if products.count() == 0:
            products = products.filter(
                Q(title__icontains=keywords) | Q(user__username__icontains=keywords))

    # if request.user.is_authenticated:
    #     try:
    #         cart = Cart.objects.get(cart_owner=request.user)
    #         cart_items_num = cart.cartitems_set.count()
    #     except:
    #         cart_items_num = 0

    context = {
        # 'cart_items_num': cart_items_num,
        'category_slug': category,
        'categories': categories,
        'companycontactdetails': companycontactdetails,
        'companysocialmedialinks': companysocialmedialinks,
        'location': location,
        'event_types': event_types,
        'products': products,
        'equipments': equipments,
        'keywords': keywords,
        'hire_cars': hire_products,
        'all_agents': clearing_agents,
    }
    return render(request, 'store/vehicles.html', context)


def submit_order(request, id, slug):
    form = OrderForm()
    categories = Category.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    equipments = Equipment.objects.filter(active=True)
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')

    # other
    product = get_object_or_404(Product, id=id, slug=slug, active=True)
    images = product.productimage_set.all()
    if request.method == 'POST':
        print('INSIDE POST METHOD')
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            print('INSIDE VALID FORM')
            print('VEHICLE ID:: ', id)
            vehicle = Product.objects.get(id=id)
            print(vehicle.title)
            # order.contact_name = request.cleaned_data.get('contact_name')
            order.vehicle_of_interest = vehicle
            order.sub_total = vehicle.price
            # order.phone_number = request.cleaned_data.get('phone_number')
            # order.email = request.cleaned_data.get('email')
            # order.country_region = request.cleaned_data.get('country_region')
            # order.city = request.cleaned_data.get('city')
            # order.street_address = request.cleaned_data.get('street_address')
            # order.province = request.cleaned_data.get('province')
            order.save()
            messages.success(request, 'Order was successfully submitted.')
            return redirect('order_request_done')

        else:
            messages.success(request, 'Invalid form submitted.')
            print('FORM NOT VALID')
            context = {
                'product': product,
                'equipments': equipments,
                'images': images,
                'categories': categories,
                'companycontactdetails': companycontactdetails,
                'companysocialmedialinks': companysocialmedialinks,
                'location': location,
                'event_types': event_types,
                'form': form,
                'all_agents': clearing_agents,
            }
            return render(request, 'store/car_detail.html', context)

    return render(request, 'store/car_detail.html')


def product_detail(request, slug):
    global cart_items_num
    # globals
    form = OrderForm()
    categories = Category.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    equipments = Equipment.objects.filter(active=True)
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')

    # other
    product = get_object_or_404(Product, slug=slug, active=True)
    images = product.productimage_set.all()

    # if request.user.is_authenticated:
    #     try:
    #         cart = Cart.objects.get(cart_owner=request.user)
    #         cart_items_num = cart.cartitems_set.count()
    #     except:
    #         cart_items_num = 0

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)

            vehicle = Product.objects.get(id=request.cleaned_data.get('vehicle_of_interest'))
            order.contact_name = request.cleaned_data.get('contact_name')
            order.vehicle_of_interest = vehicle
            order.phone_number = request.cleaned_data.get('phone_number')
            order.email = request.cleaned_data.get('email')
            order.country_region = request.cleaned_data.get('country_region')
            order.city = request.cleaned_data.get('city')
            order.street_address = request.cleaned_data.get('street_address')
            order.province = request.cleaned_data.get('province')

            #new_user.skillsbox = request.POST.get('skillsbox')

            order.save()

            return redirect('index')

        else:
            context = {
                'product': product,
                'equipments': equipments,
                'images': images,
                'categories': categories,
                'companycontactdetails': companycontactdetails,
                'companysocialmedialinks': companysocialmedialinks,
                'location': location,
                'event_types': event_types,
                'form': form,
                'all_agents': clearing_agents,
            }
            return render(request, 'store/car_detail.html', context)

    context = {
        'product': product,
        'equipments': equipments,
        'images': images,
        'categories': categories,
        'companycontactdetails': companycontactdetails,
        'companysocialmedialinks': companysocialmedialinks,
        'location': location,
        'event_types': event_types,
        'form': form,
        'all_agents': clearing_agents,
    }
    return render(request, 'store/car_detail.html', context)


def product_search(request, category_slug=None):
    global cart_items_num, vehicles, autoshopsandcarwash, events
    cart_items_num = 0
    category = None

    # globals
    categories = Category.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    equipments = Equipment.objects.filter(active=True)
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')


    # other
    getproducts = Product.objects.filter(active=True)

    keywords = request.GET.get('q')
    getcat = request.POST.get('p')

    if category_slug:
        # category = get_object_or_404(Category, slug=category_slug)
        getproducts = Product.objects.filter(category__slug=category_slug)
        category = category_slug

    # search
    if keywords:
        vehicles = getproducts.filter(
            Q(title__icontains=keywords) | Q(user__username__icontains=keywords) |
            Q(category__category_name__icontains=keywords) | Q(brand__icontains=keywords) |
            Q(listing_type__icontains=keywords) | Q(vehicle_status__icontains=keywords) |
            Q(location__location_name__icontains=keywords))

        equipments = equipments.filter(
            Q(user__username__icontains=keywords) | Q(equipment_type__equipment__equipment_name__icontains=keywords) |
            Q(equipment_name__icontains=keywords) | Q(equipment_brand__icontains=keywords))

        autoshopsandcarwash = AutoShopAndCarWash.objects.filter(
            Q(name__icontains=keywords) | Q(category__icontains=keywords) |
            Q(location__icontains=keywords))

        events = Event.objects.filter(
            Q(event_name__icontains=keywords) | Q(event_type__event__event_name__icontains=keywords) |
            Q(venue__icontains=keywords))

    products = chain(vehicles, equipments, autoshopsandcarwash, events)


    context = {
        # 'cart_items_num': cart_items_num,
        'category_slug': category,
        'categories': categories,
        'companycontactdetails': companycontactdetails,
        'companysocialmedialinks': companysocialmedialinks,
        'location': location,
        'event_types': event_types,
        'products': products,
        'equipments': equipments,
        'keywords': keywords,
        'all_agents': clearing_agents,
    }
    return render(request, 'store/search_view.html', context)


# def search_filters_brand(request, brand, keywords):
#     global cart_items_num, products
#     cart_items_num = 0
#     category = None
#     # products = Product.objects.filter(active=True)
#     # globals
#     categories = Category.objects.all()
#     companycontactdetails = CompanyContactDetails.objects.all()
#     companysocialmedialinks = CompanySocialMediaLinks.objects.all()
#     location = Location.objects.all()
#     event_types = EventType.objects.all()
#
#     # other
#
#     # search
#     # if brand:
#     #     products = products.filter(
#     #         Q(title__icontains=keywords) | Q(user__username__icontains=keywords) | Q(brand__icontains=brand))
#
#     if brand:
#         products = Product.objects.filter(
#             Q(title__icontains=keywords) | Q(user__username__icontains=keywords) and Q(brand__icontains=brand))
#
#     # if request.user.is_authenticated:
#     #     try:
#     #         cart = Cart.objects.get(cart_owner=request.user)
#     #         cart_items_num = cart.cartitems_set.count()
#     #     except:
#     #         cart_items_num = 0
#
#     context = {
#         # 'cart_items_num': cart_items_num,
#         'category_slug': category,
#         'categories': categories,
#         'companycontactdetails': companycontactdetails,
#         'companysocialmedialinks': companysocialmedialinks,
#         'location': location,
#         'event_types': event_types,
#         'products': products,
#         'keywords': keywords,
#     }
#     return render(request, 'store/search_view.html', context)


def sale_vehicles(request, category_slug=None):
    category = None

    # globals
    categories = Category.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')

    # other
    products = Product.objects.filter(active=True, listing_type='For Sale')

    keywords = request.GET.get('q')
    getcat = request.POST.get('p')

    if category_slug:
        # category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category__slug=category_slug)
        category = category_slug

    if keywords:
        products = products.filter(
            Q(title__icontains=keywords) | Q(user__username__icontains=keywords))

    context = {
        'category_slug': category,
        'categories': categories,
        'companycontactdetails': companycontactdetails,
        'companysocialmedialinks': companysocialmedialinks,
        'location': location,
        'event_types': event_types,
        'products': products,
        'keywords': keywords,
        'all_agents': clearing_agents,
    }
    return render(request, 'store/index.html', context)


def hire_vehicles(request, category_slug=None):
    category = None
    # globals
    categories = Category.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')

    # other
    products = Product.objects.filter(active=True, listing_type='For Hire')

    keywords = request.GET.get('q')
    getcat = request.POST.get('p')

    if category_slug:
        # category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category__slug=category_slug)
        category = category_slug

    if keywords:
        products = products.filter(
            Q(title__icontains=keywords) | Q(user__username__icontains=keywords))

    context = {
        'category_slug': category,
        'categories': categories,
        'companycontactdetails': companycontactdetails,
        'companysocialmedialinks': companysocialmedialinks,
        'location': location,
        'event_types': event_types,
        'products': products,
        'keywords': keywords,
        'all_agents': clearing_agents,
    }
    return render(request, 'store/index.html', context)


def classified_vehicles(request, category_slug=None):
    category = None

    # globals
    categories = Category.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')

    # other
    products = Product.objects.filter(active=True, listing_type='Classified')

    keywords = request.GET.get('q')
    getcat = request.POST.get('p')

    if category_slug:
        # category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category__slug=category_slug)
        category = category_slug

    if keywords:
        products = products.filter(
            Q(title__icontains=keywords) | Q(user__username__icontains=keywords))

    context = {
        'category_slug': category,
        'categories': categories,
        'companycontactdetails': companycontactdetails,
        'companysocialmedialinks': companysocialmedialinks,
        'location': location,
        'event_types': event_types,
        'products': products,
        'keywords': keywords,
        'all_agents': clearing_agents,
    }
    return render(request, 'store/index.html', context)


def all_events(request):
    # globals
    categories = Category.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')

    # other
    events = Event.objects.all()
    return render(request, 'events/all_events.html',
                  {
                      'events': events,
                      'categories': categories,
                      'companycontactdetails': companycontactdetails,
                      'companysocialmedialinks': companysocialmedialinks,
                      'location': location,
                      'event_types': event_types,
                      'all_agents': clearing_agents,
                  })


def event_detail(request, slug):
    # globals
    categories = Category.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')

    # other
    event = Event.objects.get(slug=slug)
    return render(request, 'events/event_details.html',
                  {
                      'event': event,
                      'categories': categories,
                      'companycontactdetails': companycontactdetails,
                      'companysocialmedialinks': companysocialmedialinks,
                      'location': location,
                      'event_types': event_types,
                      'all_agents': clearing_agents,

                  })


def all_news(request):
    # globals
    categories = Category.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')

    # other
    events = Event.objects.all()
    return render(request, 'events/all_events.html',
                  {
                      'events': events,
                      'categories': categories,
                      'companycontactdetails': companycontactdetails,
                      'companysocialmedialinks': companysocialmedialinks,
                      'location': location,
                      'event_types': event_types,
                      'all_agents': clearing_agents,
                  })

# def search_by_location(request, ):
def clearing_agents(request):
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')
    return render(request, 'agents/agents_list.html',
                  {
                      'all_agents': clearing_agents,
                  })