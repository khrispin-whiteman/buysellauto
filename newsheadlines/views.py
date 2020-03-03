from django.shortcuts import render

# Create your views here.
import requests
url = ('http://newsapi.org/v2/top-headlines?'
       'country=zm&'
       'apiKey=fa293cf0f2af400797135d78e7cb4101')
response = requests.get(url)
print (response.json())