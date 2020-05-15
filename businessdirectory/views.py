from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from aboutus.models import CompanyContactDetails, CompanySocialMediaLinks
from agents.models import Agent
from businessdirectory.models import Equipment, EquipmentType, AutoShopAndCarWash
from orders.forms import OrderForm
from store.models import EventType, Location, Product


def equipments(request, category_slug=None):
    category = None
    # globals
    form = OrderForm()
    equipment_type = EquipmentType.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')

    # other
    equipments = Equipment.objects.filter(active=True)
    #hire_products = Product.objects.filter(active=True, listing_type='For Hire')

    keywords = request.GET.get('q')
    getcat = request.POST.get('p')

    if category_slug:
        # category = get_object_or_404(Category, slug=category_slug)
        equipments = Equipment.objects.filter(category__slug=category_slug)
        category = category_slug

    if keywords:
        equipments = equipments.filter(
            Q(equipment_type__equipment_type__icontains=keywords) |
            Q(equipment_name__icontains=keywords))


    # if request.user.is_authenticated:
    #     try:
    #         cart = Cart.objects.get(cart_owner=request.user)
    #         cart_items_num = cart.cartitems_set.count()
    #     except:
    #         cart_items_num = 0

    context = {
        # 'cart_items_num': cart_items_num,
        'form': form,
        'category_slug': category,
        'categories': equipment_type,
        'companycontactdetails': companycontactdetails,
        'companysocialmedialinks': companysocialmedialinks,
        'location': location,
        'event_types': event_types,
        'products': equipments,
        'keywords': keywords,
        'clearing_agents': clearing_agents,
        #'hire_cars': hire_products,
    }
    return render(request, 'businessdirectory/equipments.html', context)


def equipment_detail(request, pk):
    form = OrderForm()
    equipment_type = EquipmentType.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    equipment_details = Equipment.objects.get(active=True, id=pk)
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')

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
                'equipment_details': equipment_details,
                'form': form,
                'category_slug': equipment_type,
                'categories': equipment_type,
                'companycontactdetails': companycontactdetails,
                'companysocialmedialinks': companysocialmedialinks,
                'location': location,
                'event_types': event_types,
                'clearing_agents': clearing_agents,
            }
            return render(request, 'businessdirectory/equipment_details.html', context)

    return render(request, 'businessdirectory/equipment_details.html',
                  {
                      'equipment_details': equipment_details,
                      'form': form,
                      'category_slug': equipment_type,
                      'categories': equipment_type,
                      'companycontactdetails': companycontactdetails,
                      'companysocialmedialinks': companysocialmedialinks,
                      'location': location,
                      'event_types': event_types,
                      'clearing_agents': clearing_agents,
                  })


def car_wash_view(request, category_slug=None):
    category = None
    # globals
    form = OrderForm()
    equipment_type = EquipmentType.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')
    car_wash = AutoShopAndCarWash.objects.filter(category='Car Wash')
    print(car_wash)

    # other
    equipments = Equipment.objects.filter(active=True)
    #hire_products = Product.objects.filter(active=True, listing_type='For Hire')

    keywords = request.GET.get('q')
    getcat = request.POST.get('p')

    if category_slug:
        # category = get_object_or_404(Category, slug=category_slug)
        equipments = Equipment.objects.filter(category__slug=category_slug)
        category = category_slug

    if keywords:
        equipments = equipments.filter(
            Q(equipment_type__equipment_type__icontains=keywords) |
            Q(equipment_name__icontains=keywords))


    # if request.user.is_authenticated:
    #     try:
    #         cart = Cart.objects.get(cart_owner=request.user)
    #         cart_items_num = cart.cartitems_set.count()
    #     except:
    #         cart_items_num = 0

    context = {
        # 'cart_items_num': cart_items_num,
        'form': form,
        'category_slug': category,
        'categories': equipment_type,
        'companycontactdetails': companycontactdetails,
        'companysocialmedialinks': companysocialmedialinks,
        'location': location,
        'event_types': event_types,
        'products': equipments,
        'keywords': keywords,
        'clearing_agents': clearing_agents,
        'car_wash': car_wash,
        #'hire_cars': hire_products,
    }
    return render(request, 'businessdirectory/car_wash.html', context)


def car_wash_detail(request, id):
    category = None
    # globals
    form = OrderForm()
    equipment_type = EquipmentType.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')
    car_wash = AutoShopAndCarWash.objects.get(id=id, category='Car Wash')
    print(car_wash)

    # other
    equipments = Equipment.objects.filter(active=True)
    #hire_products = Product.objects.filter(active=True, listing_type='For Hire')

    keywords = request.GET.get('q')
    getcat = request.POST.get('p')

    # if category_slug:
    #     # category = get_object_or_404(Category, slug=category_slug)
    #     equipments = Equipment.objects.filter(category__slug=category_slug)
    #     category = category_slug

    if keywords:
        equipments = equipments.filter(
            Q(equipment_type__equipment_type__icontains=keywords) |
            Q(equipment_name__icontains=keywords))


    # if request.user.is_authenticated:
    #     try:
    #         cart = Cart.objects.get(cart_owner=request.user)
    #         cart_items_num = cart.cartitems_set.count()
    #     except:
    #         cart_items_num = 0

    context = {
        # 'cart_items_num': cart_items_num,
        'form': form,
        'category_slug': category,
        'categories': equipment_type,
        'companycontactdetails': companycontactdetails,
        'companysocialmedialinks': companysocialmedialinks,
        'location': location,
        'event_types': event_types,
        'products': equipments,
        'keywords': keywords,
        'clearing_agents': clearing_agents,
        'car_wash': car_wash,
        #'hire_cars': hire_products,
    }
    return render(request, 'businessdirectory/car_wash_detail.html', context)


def auto_shop_view(request, category_slug=None):
    category = None
    # globals
    form = OrderForm()
    equipment_type = EquipmentType.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')
    auto_shop = AutoShopAndCarWash.objects.filter(category='Auto Shop')

    # other
    equipments = Equipment.objects.filter(active=True)
    #hire_products = Product.objects.filter(active=True, listing_type='For Hire')

    keywords = request.GET.get('q')
    getcat = request.POST.get('p')

    if category_slug:
        # category = get_object_or_404(Category, slug=category_slug)
        equipments = Equipment.objects.filter(category__slug=category_slug)
        category = category_slug

    if keywords:
        equipments = equipments.filter(
            Q(equipment_type__equipment_type__icontains=keywords) |
            Q(equipment_name__icontains=keywords))


    # if request.user.is_authenticated:
    #     try:
    #         cart = Cart.objects.get(cart_owner=request.user)
    #         cart_items_num = cart.cartitems_set.count()
    #     except:
    #         cart_items_num = 0

    context = {
        # 'cart_items_num': cart_items_num,
        'form': form,
        'category_slug': category,
        'categories': equipment_type,
        'companycontactdetails': companycontactdetails,
        'companysocialmedialinks': companysocialmedialinks,
        'location': location,
        'event_types': event_types,
        'products': equipments,
        'keywords': keywords,
        'clearing_agents': clearing_agents,
        'auto_shop': auto_shop,
        #'hire_cars': hire_products,
    }
    return render(request, 'businessdirectory/auto_shop.html', context)


def auto_shop_detail(request, id):
    category = None
    # globals
    form = OrderForm()
    equipment_type = EquipmentType.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')
    auto_shop = AutoShopAndCarWash.objects.get(id=id, category='Auto Shop')


    # other
    equipments = Equipment.objects.filter(active=True)
    #hire_products = Product.objects.filter(active=True, listing_type='For Hire')

    keywords = request.GET.get('q')
    getcat = request.POST.get('p')

    # if category_slug:
    #     # category = get_object_or_404(Category, slug=category_slug)
    #     equipments = Equipment.objects.filter(category__slug=category_slug)
    #     category = category_slug

    if keywords:
        equipments = equipments.filter(
            Q(equipment_type__equipment_type__icontains=keywords) |
            Q(equipment_name__icontains=keywords))


    # if request.user.is_authenticated:
    #     try:
    #         cart = Cart.objects.get(cart_owner=request.user)
    #         cart_items_num = cart.cartitems_set.count()
    #     except:
    #         cart_items_num = 0

    context = {
        # 'cart_items_num': cart_items_num,
        'form': form,
        'category_slug': category,
        'categories': equipment_type,
        'companycontactdetails': companycontactdetails,
        'companysocialmedialinks': companysocialmedialinks,
        'location': location,
        'event_types': event_types,
        'products': equipments,
        'keywords': keywords,
        'clearing_agents': clearing_agents,
        'auto_shop': auto_shop,
        #'hire_cars': hire_products,
    }
    return render(request, 'businessdirectory/auto_shop_detail.html', context)