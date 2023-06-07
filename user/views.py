from django.shortcuts import render, redirect
from .models import Register, Purchase
from admins.models import Products
from django.contrib import messages


# Create your views here.
def reg(request):
    if request.method == 'POST':
        try:
            uname = request.POST.get('uname')
            email = request.POST.get('email')
            paw = request.POST.get('paw')

            mno = request.POST.get('mno')
            location = request.POST.get('location')
            pincode = request.POST.get('pincode')

            data = Register(
                uname=uname,
                email=email,
                paw=paw,
                mno=mno,
                location=location,
                pincode=pincode,
            )
            data.save()
            return render(request, 'U_login.html')
        except Exception as e:
            print("Error is :", e)

    else:
        return render(request, 'U_Reg.html')


def home(request):
    return render(request, 'U_Home.html')


def ulogin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        paw = request.POST.get('paw')
        try:
            users = Register.objects.get(uname=name, paw=paw)
            request.session['userid'] = users.id
            request.session['username'] = users.uname
            print(name, paw)
            return render(request, 'U_Home.html')
        except Exception as e:
            print("Exception is :", e)
            message = "User name and password are not matching..."
        return render(request, 'U_login.html', {'msg': message})
    else:
        print("hello-2")
        return render(request, 'U_login.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def alogin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        paw = request.POST.get('paw')
        print(name, paw)
        if name == 'admin' and paw == 'admin':
            print("I am in inner")
            return render(request, 'A_Home.html')
        else:
            print("Hello")
            return render(request, 'A_login.html')
    else:
        print("hello-2")
        return render(request, 'A_login.html')


def products(request):
    product = Products.objects.all()
    return render(request, 'U_View_Products.html', {'products': product})


def buy_product(request, id):
    if request.method == 'POST':
        uid = request.session['userid']
        print(uid)
        cid = Register.objects.get(id=uid)
        id1 = cid.id

        product = Products.objects.get(id=id)
        data = Purchase(
            pname=product.pname,
            pcost=product.pcost,
            pquality=product.pquality,
            pdec=product.pdec,
            cid_id=id1,
            pid_id=id,
        )
        data.save()

        messages.success(request, 'Product purchased successfully.')
        return render(request, 'U_View_Products.html')
    else:
        messages.error(request, 'Not Purchased.')
        return redirect('products')


def purchase(request):
    if request.method == 'POST':
        uid = request.session['userid']
        pname = request.POST.get()
        price = request.POST.get()
        pstatus = request.POST.get()
        data = Purchase(
            pname=pname,
            price=price,
            pstatus=pstatus,
            uname_id=uid,
        )
        data.save()

    return redirect('user:home')


def phistory(request):
    uid = request.session['userid']
    cdata = Register.objects.get(id=uid)
    cid = cdata.id
    data = Purchase.objects.filter(cid_id=cid)
    #purchase = Purchase.objects.all()
    return render(request, 'U_Purchase_data.html', {'data':data ,'data2': cdata})


def logout(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def profile(request):
    uid = request.session['userid']
    data = Register.objects.get(id=uid)
    return render(request, 'U_Profile.html', {'profile': [data]})
