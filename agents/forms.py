from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from tinymce.widgets import TinyMCE

from agents.models import AgentType, Agent
from store.models import User


class AgentAddForm(UserCreationForm):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Username",
    )

    password1 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'class': 'form-control',
            }
        ),
        label="Password",
    )

    password2 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'class': 'form-control',
            }
        ),
        label="Confirm Password",
    )


    firstname = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Firstname",
    )

    lastname = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Lastname",
    )

    email = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Email",
    )

    address = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Address",
    )

    phone = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Mobile No.",
    )

    portfolio_site = forms.URLField(
        max_length=50,
        label='Your website',
        required=False,
        initial='http://',
        widget=forms.URLInput(attrs={
            'class': 'form-control'
        })
    )

    company_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Company Name",
    )

    country = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Country",
    )

    city = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="City",
    )

    postal_code = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Postal Code",
    )

    experience = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Experience",
    )

    # picture = forms.ImageField(
    #     widget=forms.FileInput(
    #         attrs={
    #             'type': 'file',
    #             'class': 'form-control'
    #         }
    #     )
    # )

    agent_type = forms.ModelChoiceField(queryset=AgentType.objects.all(),
                                         widget=forms.Select(
                                             attrs={'class': 'btn-block form-control',
                                                    'style': 'height: 40px;',
                                                    }),
                                         empty_label='---------------------------------------')



    description = forms.CharField(
        widget=TinyMCE(
            attrs={
                'cols': 80, 'rows': 5,
                'class': 'form-control',
            }))


    class Meta(UserCreationForm.Meta):
        model = User
        #fields = ('firstname', 'lastname', 'password1', 'password2', 'email', 'address', 'phone', 'portfolio_site', 'description')


    @transaction.atomic()
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_agent = True
        user.first_name = self.cleaned_data.get('firstname')
        user.last_name = self.cleaned_data.get('lastname')
        user.portfolio_site = self.cleaned_data.get('portfolio_site')
        user.phone = self.cleaned_data.get('phone')
        user.country = self.cleaned_data.get('country')
        user.city = self.cleaned_data.get('city')
        user.postal_code = self.cleaned_data.get('postal_code')
        user.address = self.cleaned_data.get('address')
        user.email = self.cleaned_data.get('email')
        user.picture = self.cleaned_data.get('picture')
        if commit:
            user.save()

        agent, created = Agent.objects.get_or_create(user=user, agent_type=self.cleaned_data.get('agent_type'), company_name=self.cleaned_data.get('company_name'), description=self.cleaned_data.get('description'))
        agent.save()

        return user
