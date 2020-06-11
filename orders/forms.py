from django import forms
from django.db import transaction

from orders.models import Order, EquipmentOrder
from store.models import Product


class OrderForm(forms.ModelForm):
    contact_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Full Name',
            }
        ),
        label="Full Name",
    )

    email = forms.EmailField(
        max_length=50,
        widget=forms.EmailInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'example@gmail.com',
            }
        ),
        label="Email",
    )

    phone_number = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Eg: +260970000000',
            }
        ),
        label="Mobile No.",
    )

    country_region = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Country',
            }
        ),
        label="Country",
    )

    province = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Province',
            }
        ),
        label="Province",
    )

    city = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'City',
            }
        ),
        label="City",
    )

    street_address = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Street Address',
            }
        ),
        label="Street Address",
    )

    # vehicle_of_interest = forms.CharField(
    #     max_length=50,
    #     widget=forms.TextInput(
    #         attrs={
    #             'type': 'text',
    #             'class': 'form-control',
    #             'placeholder': 'Vehicle',
    #         }
    #     ),
    #     label="Vehicle",
    # )



    # @transaction.atomic()
    # def save(self, commit=True):
    #     order = super().save(commit=False)
    #     vehicle = Product.objects.get(id=self.cleaned_data.get('vehicle_of_interest'))
    #     order.contact_name = self.cleaned_data.get('contact_name')
    #     order.vehicle_of_interest = vehicle
    #     order.phone_number = self.cleaned_data.get('phone_number')
    #     order.email = self.cleaned_data.get('email')
    #     order.country_region = self.cleaned_data.get('country_region')
    #     order.city = self.cleaned_data.get('city')
    #     order.street_address = self.cleaned_data.get('street_address')
    #     order.province = self.cleaned_data.get('province')
    #
    #     if commit:
    #         order.save()
    #
    #
    #     return order


    class Meta:
        model = Order
        fields = ['contact_name', 'email', 'phone_number', 'country_region', 'province', 'city', 'street_address',]


class EquipmentOrderForm(forms.ModelForm):
    contact_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Full Name',
            }
        ),
        label="Full Name",
    )

    email = forms.EmailField(
        max_length=50,
        widget=forms.EmailInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'example@gmail.com',
            }
        ),
        label="Email",
    )

    phone_number = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Eg: +260970000000',
            }
        ),
        label="Mobile No.",
    )

    country_region = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Country',
            }
        ),
        label="Country",
    )

    province = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Province',
            }
        ),
        label="Province",
    )

    city = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'City',
            }
        ),
        label="City",
    )

    street_address = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Street Address',
            }
        ),
        label="Street Address",
    )

    # equipment_of_interest = forms.CharField(
    #     max_length=50,
    #     widget=forms.TextInput(
    #         attrs={
    #             'type': 'text',
    #             'class': 'form-control',
    #             'placeholder': 'Equipment',
    #         }
    #     ),
    #     label="Equipment",
    # )

    # @transaction.atomic()
    # def save(self, commit=True):
    #     order = super().save(commit=False)
    #     vehicle = Product.objects.get(id=self.cleaned_data.get('vehicle_of_interest'))
    #     order.contact_name = self.cleaned_data.get('contact_name')
    #     order.vehicle_of_interest = vehicle
    #     order.phone_number = self.cleaned_data.get('phone_number')
    #     order.email = self.cleaned_data.get('email')
    #     order.country_region = self.cleaned_data.get('country_region')
    #     order.city = self.cleaned_data.get('city')
    #     order.street_address = self.cleaned_data.get('street_address')
    #     order.province = self.cleaned_data.get('province')
    #
    #     if commit:
    #         order.save()
    #
    #
    #     return order

    class Meta:
        model = EquipmentOrder
        fields = ['contact_name', 'email', 'phone_number', 'country_region', 'province', 'city', 'street_address',
                  ]
