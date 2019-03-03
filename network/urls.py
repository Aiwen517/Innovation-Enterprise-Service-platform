"""network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from culture import views


urlpatterns = [

    #url(r'^home/', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'login', views.login, name='login'),
    url(r'signup', views.signup, name='signup'),
    url(r'News', views.News, name='News'),
    url(r'News1', views.News1, name='News1'),
    url(r'exhibition', views.exhibition, name='exhibition'),
    url(r'exhibition1', views.exhibition1, name='exhibition1'),
    url(r'product', views.product, name='product'),
    url(r'PersonProduct', views.PersonProduct, name='PersonProduct'),
    url(r'PersonProductDetail', views.PersonProductDetail, name='PersonProductDetail'),
    url(r'CompanyProduct', views.CompanyProduct, name='CompanyProduct'),
    url(r'CompanyProductDetail', views.CompanyProductDetail, name='CompanyProductDetail'),
    url(r'Needs', views.Needs, name='Needs'),
    url(r'PersonNeeds', views.PersonNeeds, name='PersonNeeds'),
    url(r'PersonNeedsDetail', views.PersonNeedsDetail, name='PersonNeedsDetail'),
    url(r'CompanyProduct', views.CompanyProduct, name='CompanyProduct'),
    url(r'CompanyProductDetail', views.CompanyProductDetail, name='CompanyProductDetail'),
    url(r'', views.index),
]
