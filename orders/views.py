from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView

from aboutus.models import CompanySocialMediaLinks, CompanyContactDetails
from agents.models import Agent
from businessdirectory.models import Equipment
from orders.forms import OrderForm, EquipmentOrderForm
from orders.models import Order


# Create your views here.
from store.models import Location, Category, EventType


def order_request_done(request):
    return render(request, 'orders/order_request_done.html', {})


def submit_equipment_order(request, id, slug):
    form = EquipmentOrderForm()
    categories = Category.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    location = Location.objects.all()
    event_types = EventType.objects.all()
    equipments = Equipment.objects.filter(active=True)
    clearing_agents = Agent.objects.filter(agent_type__agent_type='Clearing Agent')

    # other
    equipment = get_object_or_404(Equipment, id=id, slug=slug, active=True)
    images = equipment.equipmentimage_set.all()
    if request.method == 'POST':
        print('INSIDE POST METHOD')
        form = EquipmentOrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            print('INSIDE VALID FORM')
            print('VEHICLE ID:: ', id)
            equipment = Equipment.objects.get(id=id)
            print(equipment.equipment_name)
            # order.contact_name = request.cleaned_data.get('vehicle_of_interest')
            order.equipment_of_interest = equipment
            order.sub_total = equipment.equipment_price

            order.save()
            messages.success(request, 'Order was successfully submitted.')
            return redirect('order_request_done')

        else:
            messages.success(request, 'Invalid form submitted.')
            print('FORM NOT VALID')
            context = {
                'equipment_details': equipment,
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
            return render(request, 'businessdirectory/equipment_details.html', context)

    return render(request, 'businessdirectory/equipment_details.html')


class OrderRequestView(CreateView):
    model = Order
    form_class = OrderForm
    # teachers = User.objects.get(is_lecturer=False)
    template_name = 'store/car_detail.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'class'
        #kwargs['teachers'] = User.objects.filter(is_lecturer=True)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return redirect('order_request_done')


class EquipmentOrderRequestView(CreateView):
    model = Order
    form_class = OrderForm
    # teachers = User.objects.get(is_lecturer=False)
    template_name = 'businessdirectory/equipment_details.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'class'
        #kwargs['teachers'] = User.objects.filter(is_lecturer=True)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return redirect('order_request_done')


