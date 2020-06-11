from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponse
from aboutus.models import CompanyContactDetails, CompanySocialMediaLinks
from agents.models import Agent
from businessdirectory.models import Equipment, EquipmentType, AutoShopAndCarWash, FillingStation, FinancialInstitution, \
    MotorisedService, AutoEngineering, EarthMoving, Training, Transportation, FillingStationDirectory, \
    FinancialInstitutionDirectory
from orders.forms import OrderForm
from store.models import EventType, Location, Product
from django.core.mail import send_mail as sm
#from mailjet_rest import Client
import os
# from __future__ import print_function
# import time
# import sib_api_v3_sdk
# from sib_api_v3_sdk.rest import ApiException
# from pprint import pprint

# Create your views here.
# def send_mail(request):
#     sib_api_v3_sdk.configuration.api_key['api-key'] = 'YOUR_API_V3_KEY'
#     api_instance = sib_api_v3_sdk.EmailCampaignsApi()
#     # Define the campaign settings\
#     email_campaigns = sib_api_v3_sdk.CreateEmailCampaign(
#         name="Campaign sent via the API",
#         subject="My subject",
#         sender={"name": "From name", "email": "khrispinwhiteman@gmail.com"},
#         type="classic",
#         # Content that will be sent\
#         html_content="Congratulations! You successfully sent this example campaign via the Sendinblue API.",
#         # Select the recipients\
#         recipients={"listIds": [2, 7]},
#         # Schedule the sending in one hour\
#         scheduled_at="2018-01-01 00:00:01"
#     )
#     # Make the call to the client\
#     try:
#         api_response = api_instance.create_email_campaign(email_campaigns)
#     pprint(api_response)
#     except ApiException as e:
#     print("Exception when calling EmailCampaignsApi->create_email_campaign: %s\n" % e)
#
#     return HttpResponse(f"Email sent to {res} members")


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
        equipments = Equipment.objects.filter(equipment_type__slug=category_slug)
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


def equipment_detail(request, slug):
    form = OrderForm()
    equipment_type = EquipmentType.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    equipment_details = Equipment.objects.get(active=True, slug=slug)
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


def car_wash_detail(request, slug):
    category = None
    # globals
    form = OrderForm()
    equipment_type = EquipmentType.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')
    car_wash = AutoShopAndCarWash.objects.get(slug=slug, category='Car Wash')
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


def auto_shop_detail(request, slug):
    category = None
    # globals
    form = OrderForm()
    equipment_type = EquipmentType.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')
    auto_shop = AutoShopAndCarWash.objects.get(slug=slug, category='Auto Shop')


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
def filling_stations_list(request, category_slug=None):
    category = None
    filling_stations_directory = FillingStationDirectory.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')
    filling_stations = FillingStation.objects.all()


    if category_slug:
        # category = get_object_or_404(Category, slug=category_slug)
        filling_stations = FillingStation.objects.filter(location=category_slug)
        category = category_slug


    keywords = request.GET.get('q')
    if keywords:
        filling_stations = filling_stations.filter(
            Q(name__filling_station_name__icontains=keywords) | Q(location__icontains=keywords))

    return render(request, 'businessdirectory/filling_stations/filling_station_list.html',
                  {
                      'category_slug': category,
                      'categories': filling_stations_directory,
                      'companycontactdetails': companycontactdetails,
                      'companysocialmedialinks': companysocialmedialinks,
                      'location': location,
                      'event_types': event_types,
                      'clearing_agents': clearing_agents,
                      'filling_stations': filling_stations,
                      'keywords': keywords,
                  })


# filling station detail
def filling_stations_detail(request, slug, name, category_slug=None):
    filling_station = FillingStation.objects.get(slug=slug)
    other_filling_stations = FillingStation.objects.filter(name=filling_station.name)

    category = None
    filling_stations_directory = FillingStationDirectory.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')

    return render(request, 'businessdirectory/filling_stations/filling_station_detail.html',
                  {
                      'filling_station': filling_station,
                      'other_filling_stations': other_filling_stations,
                      'category_slug': category,
                      'categories': filling_stations_directory,
                      'companycontactdetails': companycontactdetails,
                      'companysocialmedialinks': companysocialmedialinks,
                      'location': location,
                      'event_types': event_types,
                      'clearing_agents': clearing_agents,
                  })


# financial station list
def financial_institutions_list(request, category_slug=None):
    financial_institutions = FinancialInstitution.objects.all()
    category = None
    filling_stations_directory = FillingStationDirectory.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')

    if category_slug:
        # category = get_object_or_404(Category, slug=category_slug)
        financial_institutions = FinancialInstitution.objects.filter(location=category_slug)
        category = category_slug

    keywords = request.GET.get('q')
    if keywords:
        financial_institutions = financial_institutions.filter(
            Q(name__financial_institution_name__icontains=keywords) | Q(location__icontains=keywords))

    return render(request, 'businessdirectory/financial_institutions/financial_institutions_list.html',
                  {
                      'financial_institutions': financial_institutions,
                      'keywords': keywords,
                      'category_slug': category,
                      'categories': filling_stations_directory,
                      'companycontactdetails': companycontactdetails,
                      'companysocialmedialinks': companysocialmedialinks,
                      'location': location,
                      'event_types': event_types,
                      'clearing_agents': clearing_agents,
                  })


# financial station list
def financial_institutions_detail(request, slug, name, category_slug=None):
    financial_institution = FinancialInstitution.objects.get(slug=slug)
    other_financial_institutions = FinancialInstitution.objects.filter(name=financial_institution.name)
    category = None
    financial_institutions_directory = FinancialInstitutionDirectory.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')

    return render(request, 'businessdirectory/financial_institutions/financial_institution_detail.html',
                  {
                      'financial_institution': financial_institution,
                      'other_financial_institutions': other_financial_institutions,
                      'category_slug': category,
                      'categories': financial_institutions_directory,
                      'companycontactdetails': companycontactdetails,
                      'companysocialmedialinks': companysocialmedialinks,
                      'location': location,
                      'event_types': event_types,
                      'clearing_agents': clearing_agents,
                  })


# motorized_service list
def motorized_services_list(request,):
    motorized_services = MotorisedService.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')

    keywords = request.GET.get('q')
    if keywords:
        motorized_services = motorized_services.filter(
            Q(name__icontains=keywords) | Q(location__icontains=keywords) |
            Q(city__location_name__icontains=keywords))

    return render(request, 'businessdirectory/motorized_services/motorized_services_list.html',
                  {
                      'motorized_services': motorized_services,
                      'keywords': keywords,
                      'companycontactdetails': companycontactdetails,
                      'companysocialmedialinks': companysocialmedialinks,
                      'location': location,
                      'event_types': event_types,
                      'clearing_agents': clearing_agents,
                  })


# motorized_service detail
def motorized_service_detail(request, slug):
    motorized_service = MotorisedService.objects.get(slug=slug)
    other_motorized_services = MotorisedService.objects.filter(city=motorized_service.city)
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')
    return render(request, 'businessdirectory/motorized_services/motorized_service_detail.html',
                  {
                      'motorized_service': motorized_service,
                      'other_motorized_services': other_motorized_services,
                      'companycontactdetails': companycontactdetails,
                      'companysocialmedialinks': companysocialmedialinks,
                      'location': location,
                      'event_types': event_types,
                      'clearing_agents': clearing_agents,
                  })


# auto_engineering_list
def auto_engineering_list(request):
    auto_engineerings = AutoEngineering.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')
    keywords = request.GET.get('q')
    if keywords:
        auto_engineerings = auto_engineerings.filter(
            Q(name__icontains=keywords) | Q(location__icontains=keywords) |
            Q(city__location_name__icontains=keywords))

    return render(request, 'businessdirectory/auto_engineerings/auto_engineerings_list.html',
                  {
                      'auto_engineerings': auto_engineerings,
                      'keywords': keywords,
                      'companycontactdetails': companycontactdetails,
                      'companysocialmedialinks': companysocialmedialinks,
                      'location': location,
                      'event_types': event_types,
                      'clearing_agents': clearing_agents,
                  })


# auto_engineering_detail
def auto_engineering_detail(request, slug):
    auto_engineering = AutoEngineering.objects.get(slug=slug)
    other_auto_engineerings = AutoEngineering.objects.filter(city=auto_engineering.city)
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')
    return render(request, 'businessdirectory/auto_engineerings/auto_engineering_detail.html',
                  {
                      'auto_engineering': auto_engineering,
                      'other_auto_engineerings': other_auto_engineerings,
                      'companycontactdetails': companycontactdetails,
                      'companysocialmedialinks': companysocialmedialinks,
                      'location': location,
                      'event_types': event_types,
                      'clearing_agents': clearing_agents,
                  })

# auto_engineering_list
def earth_moving_list(request):
    earth_movings = EarthMoving.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')
    keywords = request.GET.get('q')
    if keywords:
        earth_movings = earth_movings.filter(
            Q(name__icontains=keywords) | Q(location__icontains=keywords) |
            Q(city__location_name__icontains=keywords))

    return render(request, 'businessdirectory/earth_moving/earth_moving_list.html',
                  {
                      'earth_movings': earth_movings,
                      'keywords': keywords,
                      'companycontactdetails': companycontactdetails,
                      'companysocialmedialinks': companysocialmedialinks,
                      'location': location,
                      'event_types': event_types,
                      'clearing_agents': clearing_agents,
                  })


# auto_engineering_detail
def earth_moving_detail(request, slug):
    earth_moving = EarthMoving.objects.get(slug=slug)
    other_earth_movings = EarthMoving.objects.filter(city=earth_moving.city)
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')
    return render(request, 'businessdirectory/earth_moving/earth_moving_detail.html',
                  {
                      'earth_moving': earth_moving,
                      'other_earth_movings': other_earth_movings,
                      'companycontactdetails': companycontactdetails,
                      'companysocialmedialinks': companysocialmedialinks,
                      'location': location,
                      'event_types': event_types,
                      'clearing_agents': clearing_agents,
                  })


# auto_engineering_list
def training_services_list(request):
    training_services = Training.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')
    keywords = request.GET.get('q')
    if keywords:
        training_services = training_services.filter(
            Q(name__icontains=keywords) | Q(location__icontains=keywords) |
            Q(city__location_name__icontains=keywords))

    return render(request, 'businessdirectory/training_services/training_services_list.html',
                  {
                      'training_services': training_services,
                      'keywords': keywords,
                      'companycontactdetails': companycontactdetails,
                      'companysocialmedialinks': companysocialmedialinks,
                      'location': location,
                      'event_types': event_types,
                      'clearing_agents': clearing_agents,
                  })


# auto_engineering_detail
def training_service_detail(request, slug):
    training_service = Training.objects.get(slug=slug)
    other_training_services = Training.objects.filter(city=training_service.city)
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')
    return render(request, 'businessdirectory/training_services/training_service_detail.html',
                  {
                      'training_service': training_service,
                      'other_training_services': other_training_services,
                      'companycontactdetails': companycontactdetails,
                      'companysocialmedialinks': companysocialmedialinks,
                      'location': location,
                      'event_types': event_types,
                      'clearing_agents': clearing_agents,
                  })


# transportation_services_list
def transportation_services_list(request):
    transportation_services = Transportation.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')
    keywords = request.GET.get('q')
    if keywords:
        transportation_services = transportation_services.filter(
            Q(name__icontains=keywords) | Q(location__icontains=keywords) |
            Q(city__location_name__icontains=keywords))

    return render(request, 'businessdirectory/transportation_services/transportation_services_list.html',
                  {
                      'transportation_services': transportation_services,
                      'keywords': keywords,
                      'companycontactdetails': companycontactdetails,
                      'companysocialmedialinks': companysocialmedialinks,
                      'location': location,
                      'event_types': event_types,
                      'clearing_agents': clearing_agents,
                  })


# auto_engineering_detail
def transportation_service_detail(request, slug):
    transportation_service = Transportation.objects.get(slug=slug)
    other_transportation_services = Transportation.objects.filter(city=transportation_service.city)
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')
    return render(request, 'businessdirectory/transportation_services/transportation_service_detail.html',
                  {
                      'transportation_service': transportation_service,
                      'other_transportation_services': other_transportation_services,
                      'companycontactdetails': companycontactdetails,
                      'companysocialmedialinks': companysocialmedialinks,
                      'location': location,
                      'event_types': event_types,
                      'clearing_agents': clearing_agents,
                  })