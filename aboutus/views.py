from django.shortcuts import render

from aboutus.models import CompanyContactDetails, CompanySocialMediaLinks
from store.models import Category


# Create your views here.
def contactus(request):
    categories = Category.objects.all()
    companycontactdetails = CompanyContactDetails.objects.all()
    companysocialmedialinks = CompanySocialMediaLinks.objects.all()
    return render(request, 'aboutus/contact.html',
                  {
                      'categories': categories,
                      'companycontactdetails': companycontactdetails,
                      'companysocialmedialinks': companysocialmedialinks,
                  })


def feedback(request):
    return render(request, 'aboutus/feedback.html', {})


def legal(request):
    return render(request, 'aboutus/legal.html', {})


def disclaimer(request):
    return render(request, 'aboutus/disclaimer.html', {})


def payment_methods(request):
    return render(request, 'aboutus/payment_methods.html', {})


def privacy(request):
    return render(request, 'aboutus/privacy.html', {})


def security(request):
    return render(request, 'aboutus/security.html', {})
