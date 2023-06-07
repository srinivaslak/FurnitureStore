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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from user import views as v
from admins import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('admins', include('admins.urls')),

    path('home', views.home, name='home'),
    path('', v.index, name='index'),
    path('login/', v.ulogin, name='ulogin'),
    path('Register/', v.reg, name='reg'),
    path('alogin', v.alogin, name='alogin'),
    path('purchase/', v.purchase, name='purchase'),
    path('phistory/', v.phistory, name='phistory'),
    path('contact/', v.contact, name='contact'),
    path('profile/', v.profile, name='profile'),
    path('products/', v.products, name='products'),
    path('logout', v.logout, name='logout'),
    path('buyproduct/<int:id>/buy/', v.buy_product, name='buy_product'),
]

# Add static and media URL patterns for development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
