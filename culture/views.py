
# Create your views here.
from django.shortcuts import render,render_to_response
from django.http import HttpResponse

from culture import models

def index(request):
    return render_to_response('culture/homepage.html')

def login(request):
   # f = forms.asd()
    return render_to_response('culture/login.html', {})
# Create your views here.

def signup(request):
    return render_to_response('culture/sign-up.html', {})

def News(request):
    return render_to_response('culture/News.html', {})

def News1(request):
    return render_to_response('culture/News1.html')

def exhibition(request):
    return render_to_response('culture/exhibition.html')

def exhibition1(request):
    return render_to_response('culture/exhibition1.html')

def product(request):
    return render_to_response('culture/product.html')

def PersonProduct(request):
    return render_to_response('culture/PersonProduct.html', {})

def PersonProductDetail(request):
    return render_to_response('culture/PersonProductDetail.html', {})

def CompanyProduct(request):
    return render_to_response('culture/CompanyProduct.html', {})

def CompanyProductDetail(request):
    return render_to_response('culture/CompanyProductDetail.html', {})

def Needs(request):
    return render_to_response('culture/Needs.html')

def PersonNeeds(request):
    return render_to_response('culture/PersonNeeds.html')

def PersonNeedsDetail(request):
    return render_to_response('culture/PersonNeedsDetail.html')

def CompanyNeeds(request):
    return render_to_response('culture/CompanyNeeds.html')

def CompanyNeedsDetail(request):
    return render_to_response('culture/CompanyNeedsDetail.html')


