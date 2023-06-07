from django.shortcuts import render, redirect
from .models import Products
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
from user.models import Purchase,Register
from .models import Products

import io


# Create your views here.
def home(request):
    return render(request, 'A_Home.html')


def logout(request):
    return render(request, 'index.html')


def upload(request):
    if request.method == 'POST':
        try:
            pname = request.POST.get('pname')
            pcat = request.POST.get('pcategory')
            pquality = request.POST.get('pquality')
            pdec = request.POST.get('pdec')
            pcost = request.POST.get('price')
            pimage = request.FILES['pimage']

            data = Products(
                pname=pname,
                pcat=pcat,
                pcost=pcost,
                pquality=pquality,
                pdec=pdec,
                pimage=pimage,

            )
            data.save()
            return redirect('admins:products')
        except Exception as e:
            print("Exception is ", e)
            return render(request, 'A_add_product.html')
    else:
        return render(request, 'A_add_product.html')


def products(request):
    products = Products.objects.all()
    return render(request, 'A_view_product.html', {'products': products})


def purchase(request):
    data = Purchase.objects.all()
    return render(request, 'A_view_purchases.html', {'data':data })


def index(request):
    return render(request,'index.html')