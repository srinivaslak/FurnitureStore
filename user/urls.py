"""FurnitureStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views

app_name = 'user'
urlpatterns = {
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('index/',views.index,name='index'),
    path('login/', views.ulogin, name='ulogin'),
    path('Register/', views.reg, name='reg'),
    path('alogin', views.alogin, name='alogin'),
    path('purchase/', views.purchase, name='purchase'),
    path('phistory/', views.phistory, name='phistory'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('products/', views.products, name='products'),
    path('logout', views.logout, name='logout'),

}
