from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import product
from django.utils import timezone
def home(request):
    return render(request, 'products/home.html')

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon']:
            Product = product()
            Product.title = request.POST['title']
            Product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                Product.url = request.POST['url']
            else:
                Product.url = 'http://' + request.POST['url']
            Product.icon = request.FILES['icon']
            Product.image = request.FILES['image']
            Product.pub_date = timezone.datetime.now()
            Product.hunter = request.user
            Product.save()
            return redirect('home')
        else:
            return render(request, 'products/create.htm', {'error':'please fill all the fields'})

    else:
        return render(request, 'products/create.html')