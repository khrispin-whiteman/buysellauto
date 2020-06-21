from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from agents.forms import AgentAddForm
from agents.models import Agent, AgentType
from businessdirectory.models import Equipment
from orders.models import Order
from store.decorators import agent_required
from store.models import User, Product
from django.views.generic import CreateView


# class AgentRegisterView(View):
#     def get(self, request):
#         return render(request, 'registration/agent_registration.html', { 'form': AgentAddForm() })
#
#     def post(self, request):
#         form = AgentAddForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect(reverse('login'))
#
#         return render(request, 'registration/agent_registration.html', { 'form': form })


class AgentRegisterView(CreateView):
    model = User
    form_class = AgentAddForm
    template_name = 'registration/agent_registration.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'staff'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):

        user = form.save()
        # if self.request.FILES:
        #     user.picture = self.request.FILES['picture']
        # user.save()
        return redirect('login')


class AgentLoginView(View):
    def get(self, request):
        return render(request, 'registration/agent_login.html', {'form':  AuthenticationForm})

    # really low level
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user is None:
                return render(
                    request,
                    'registration/agent_login.html',
                    { 'form': form, 'invalid_creds': True }
                )

            try:
                form.confirm_login_allowed(user)
            except ValidationError:
                return render(
                    request,
                    'registration/agent_login.html',
                    { 'form': form, 'invalid_creds': True }
                )
            login(request, user)

            return redirect(reverse('agentdashboard'))


@login_required
def agent_dashboard(request):
    all_vehicles = Product.objects.filter(user__id=request.user.id)
    print(request.user.username, all_vehicles.count())
    active_vehicles = Product.objects.filter(user=request.user, active=True)
    all_equipments = Equipment.objects.filter(user=request.user)
    active_equipments = Equipment.objects.filter(user=request.user, active=True)
    #orders = Order.objects.filter(vehicle_of_interest__user__product=request.user)

    return render(request, 'agents/dashboard.html',
                  {
                      'all_vehicles': all_vehicles,
                      'active_vehicles': active_vehicles,
                      'all_equipments': all_equipments,
                      'active_equipments': active_equipments,
                      # 'orders': orders
                  })


@agent_required
def agent_profile(request):
    agent = Agent.objects.get(user=request.user)
    agent_types = AgentType.objects.all()
    user = request.user.id
    user = User.objects.get(pk=user)
    form = AgentAddForm()
    if request.method == 'POST':
        form = AgentAddForm(request.POST)
        if form.is_valid():
            # update user
            # user.first_name = request.POST.get('first_name')
            # user.last_name = request.POST.get('last_name')
            # user.email = request.POST.get('email')
            # user.phone = request.POST.get('phone')
            # user.portfolio_site = request.POST.get('portfolio_site')
            # user.country = request.POST.get('country')
            # user.city = request.POST.get('city')
            # user.address = request.POST.get('address')
            # user.postal_code = request.POST.get('postal_code')
            # user.picture = request.POST.get('picture')
            if request.FILES:
                user.picture = request.FILES['picture']
            user.save()

            # update agent
            print('AGENT TYPE ID: ', request.POST.get('agent_type'))
            get_agent_type = AgentType.objects.get(id=request.POST.get('agent_type'))

            agent.company_name = request.POST.get('company_name')
            agent.agent_type = get_agent_type
            agent.experience = request.POST.get('experience')
            agent.description = request.POST.get('description')
            agent.save()

            messages.success(request, 'Your profile was successfully edited.')
            return redirect("/profile/")

        else:
            form = AgentAddForm(instance=User, initial={
                'firstname': user.first_name,
                'lastname': user.last_name,
                'email': user.email,
                'phone': user.phone,
                'portfolio_site': user.portfolio_site,
                'country': user.country,
                'city': user.city,
                'address': user.address,
                'postal_code': user.postal_code,
                'picture': user.picture,
            })
    return render(request, 'agents/agent_profile.html',
                  {
                      'agent': agent,
                      'agent_types': agent_types,
                      'form': form
                  })


@login_required
def agent_profile_update(request):
    """ Check if the fired request is a POST then grab changes and update the records otherwise we show an empty form """
    user = request.user.id
    user = User.objects.get(pk=user)
    agent = Agent.objects.get(user=user)
    agent_types = AgentType.objects.all()
    form = AgentAddForm()

    if request.method == 'POST':
        # form = AgentAddForm(request.POST)
        # if form.is_valid():
        # update user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.portfolio_site = request.POST.get('portfolio_site')
        user.country = request.POST.get('country')
        user.city = request.POST.get('city')
        user.address = request.POST.get('address')
        user.postal_code = request.POST.get('postal_code')
        #user.picture = request.FILES.get['picture']
        if request.FILES:
            user.picture = request.FILES['picture']
        user.save()

        # update agent
        print('AGENT TYPE ID: ', request.POST.get('agent_type'))
        get_agent_type = AgentType.objects.get(id=request.POST.get('agent_type'))

        agent.company_name = request.POST.get('company_name')
        agent.agent_type = get_agent_type
        agent.experience = request.POST.get('experience')
        agent.description = request.POST.get('description')
        agent.save()

        messages.success(request, 'Your profile was successfully edited.')
        return redirect("/profile/")

        # else:
        #     form = AgentAddForm(instance=User, initial={
        #         'first_name': user.first_name,
        #         'last_name': user.last_name,
        #         'email': user.email,
        #         'phone': user.phone,
        #         'portfolio_site': user.portfolio_site,
        #         'country': user.country,
        #         'city': user.city,
        #         'address': user.address,
        #         'postal_code': user.postal_code,
        #         'picture': user.picture,
        #     })

    return render(request, 'agents/agent_profile.html',
                  {
                      'agent': agent,
                      'agent_types': agent_types,
                      'form': form
                  })



@agent_required
def agent_vehicles(request):
    all_vehicles = Product.objects.filter(user__id=request.user.id)
    return render(request, 'agents/agent_vehicles.html',
                  {
                      'all_vehicles': all_vehicles,
                  })


@agent_required
def agent_vehicle_detail(request, pk):
    vehicle_details = Product.objects.get(user=request.user, id=pk)
    return render(request, 'agents/agent_vehicle_details.html',
                  {
                      'vehicle_details': vehicle_details,
                  })


@agent_required
def agent_equipments(request):
    all_equipments = Equipment.objects.filter(user=request.user)
    return render(request, 'agents/agent_equipments.html',
                  {
                      'all_equipments': all_equipments,
                  })


@agent_required
def agent_equipment_detail(request, pk):
    equipment_details = Equipment.objects.get(user=request.user, id=pk)
    return render(request, 'agents/agent_equipment_detail.html',
                  {
                      'equipment_details': equipment_details,
                  })


def agents_list(request):
    all_agents = Agent.objects.all()
    return render(request, 'agents/agents_list.html',
                  {
                      'all_agents': all_agents,
                  })


def agents_details(request, pk):
    agent_details = Agent.objects.get(user__id=pk)
    return render(request, 'agents/agents_details.html',
                  {
                      'agent_details': agent_details,
                  })