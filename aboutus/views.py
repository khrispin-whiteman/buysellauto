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