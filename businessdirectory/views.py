from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponse
from aboutus.models import CompanyContactDetails, CompanySocialMediaLinks
from agents.models import Agent
from businessdirectory.models import Equipment, EquipmentType, AutoShopAndCarWash, FillingStation, FinancialInstitution, \
    MotorisedService, AutoEngineering, EarthMoving, Training, Transportation
from orders.forms import OrderForm
from store.models import EventType, Location, Product
from django.core.mail import send_mail as sm


# Create your views here.
def send_mail(request):
    res = sm(
        subject = 'Subject Test',
        message = 'Hello whiteman, just testing sending of emails via gmail smtp with django.',
        from_email = 'chrispinkay@gmail.com',
        recipient_list = ['khrispinwhiteman@gmail.com'],
        fail_silently=False,
    )

    return HttpResponse(f"Email sent to {res} members")


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


# filling station list
def filling_stations_list(request):
    filling_stations = FillingStation.objects.all()
    keywords = request.GET.get('q')
    if keywords:
        filling_stations = filling_stations.filter(
            Q(name__filling_station_name__icontains=keywords) | Q(location__icontains=keywords))

    return render(request, 'businessdirectory/filling_stations/filling_station_list.html',
                  {
                      'filling_stations': filling_stations,
                      'keywords': keywords,
                  })


# filling station detail
def filling_stations_detail(request, id):
    filling_station = FillingStation.objects.get(id=id)
    other_filling_stations = FillingStation.objects.filter(name=filling_station.name)
    return render(request, 'businessdirectory/filling_stations/filling_station_detail.html',
                  {
                      'filling_station': filling_station,
                      'other_filling_stations': other_filling_stations,
                  })


# financial station list
def financial_institutions_list(request):
    financial_institutions = FinancialInstitution.objects.all()
    keywords = request.GET.get('q')
    if keywords:
        financial_institutions = financial_institutions.filter(
            Q(name__financial_institution_name__icontains=keywords) | Q(location__icontains=keywords))

    return render(request, 'businessdirectory/financial_institutions/financial_institutions_list.html',
                  {
                      'financial_institutions': financial_institutions,
                      'keywords': keywords,
                  })


# financial station list
def financial_institutions_detail(request, id):
    financial_institution = FinancialInstitution.objects.get(id=id)
    other_financial_institutions = FinancialInstitution.objects.filter(name=financial_institution.name)
    return render(request, 'businessdirectory/financial_institutions/financial_institution_detail.html',
                  {
                      'financial_institution': financial_institution,
                      'other_financial_institutions': other_financial_institutions,
                  })


# motorized_service list
def motorized_services_list(request):
    motorized_services = MotorisedService.objects.all()
    keywords = request.GET.get('q')
    if keywords:
        motorized_services = motorized_services.filter(
            Q(name__icontains=keywords) | Q(location__icontains=keywords) |
            Q(city__location_name__icontains=keywords))

    return render(request, 'businessdirectory/motorized_services/motorized_services_list.html',
                  {
                      'motorized_services': motorized_services,
                      'keywords': keywords,
                  })


# motorized_service detail
def motorized_service_detail(request, id):
    motorized_service = MotorisedService.objects.get(id=id)
    other_motorized_services = MotorisedService.objects.filter(city=motorized_service.city)
    return render(request, 'businessdirectory/motorized_services/motorized_service_detail.html',
                  {
                      'motorized_service': motorized_service,
                      'other_motorized_services': other_motorized_services,
                  })


# auto_engineering_list
def auto_engineering_list(request):
    auto_engineerings = AutoEngineering.objects.all()
    keywords = request.GET.get('q')
    if keywords:
        auto_engineerings = auto_engineerings.filter(
            Q(name__icontains=keywords) | Q(location__icontains=keywords) |
            Q(city__location_name__icontains=keywords))

    return render(request, 'businessdirectory/auto_engineerings/auto_engineerings_list.html',
                  {
                      'auto_engineerings': auto_engineerings,
                      'keywords': keywords,
                  })


# auto_engineering_detail
def auto_engineering_detail(request, id):
    auto_engineering = AutoEngineering.objects.get(id=id)
    other_auto_engineerings = AutoEngineering.objects.filter(city=auto_engineering.city)
    return render(request, 'businessdirectory/auto_engineerings/auto_engineering_detail.html',
                  {
                      'auto_engineering': auto_engineering,
                      'other_auto_engineerings': other_auto_engineerings,
                  })

# auto_engineering_list
def earth_moving_list(request):
    earth_movings = EarthMoving.objects.all()
    keywords = request.GET.get('q')
    if keywords:
        earth_movings = earth_movings.filter(
            Q(name__icontains=keywords) | Q(location__icontains=keywords) |
            Q(city__location_name__icontains=keywords))

    return render(request, 'businessdirectory/earth_moving/earth_moving_list.html',
                  {
                      'earth_movings': earth_movings,
                      'keywords': keywords,
                  })


# auto_engineering_detail
def earth_moving_detail(request, id):
    earth_moving = EarthMoving.objects.get(id=id)
    other_earth_movings = EarthMoving.objects.filter(city=earth_moving.city)
    return render(request, 'businessdirectory/earth_moving/earth_moving_detail.html',
                  {
                      'earth_moving': earth_moving,
                      'other_earth_movings': other_earth_movings,
                  })


# auto_engineering_list
def training_services_list(request):
    training_services = Training.objects.all()
    keywords = request.GET.get('q')
    if keywords:
        training_services = training_services.filter(
            Q(name__icontains=keywords) | Q(location__icontains=keywords) |
            Q(city__location_name__icontains=keywords))

    return render(request, 'businessdirectory/training_services/training_services_list.html',
                  {
                      'training_services': training_services,
                      'keywords': keywords,
                  })


# auto_engineering_detail
def training_service_detail(request, id):
    training_service = Training.objects.get(id=id)
    other_training_services = Training.objects.filter(city=training_service.city)
    return render(request, 'businessdirectory/training_services/training_service_detail.html',
                  {
                      'training_service': training_service,
                      'other_training_services': other_training_services,
                  })


# transportation_services_list
def transportation_services_list(request):
    transportation_services = Transportation.objects.all()
    keywords = request.GET.get('q')
    if keywords:
        transportation_services = transportation_services.filter(
            Q(name__icontains=keywords) | Q(location__icontains=keywords) |
            Q(city__location_name__icontains=keywords))

    return render(request, 'businessdirectory/transportation_services/transportation_services_list.html',
                  {
                      'transportation_services': transportation_services,
                      'keywords': keywords,
                  })


# auto_engineering_detail
def transportation_service_detail(request, id):
    transportation_service = Transportation.objects.get(id=id)
    other_transportation_services = Transportation.objects.filter(city=transportation_service.city)
    return render(request, 'businessdirectory/transportation_services/transportation_service_detail.html',
                  {
                      'transportation_service': transportation_service,
                      'other_transportation_services': other_transportation_services,
                  })