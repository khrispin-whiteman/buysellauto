from django.shortcuts import render, redirect
from django.views.generic import CreateView
from orders.forms import OrderForm
from orders.models import Order


# Create your views here.
def order_request_done(request):
    return render(request, 'orders/order_request_done.html', {})


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