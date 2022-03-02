from django.shortcuts import render,redirect
from pages.models import customers
from pages.forms import addform

# Create your views here.
def home(request):
    customerlist = customers.objects.all()
    return render(request,'page/home.html', {'customerlist': customerlist})

def about(request):
    return render(request,'page/about.html')    

def contact(request):
    return render(request,'page/contact.html')    

def create(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']

        form = customers(first_name=firstname, last_name=lastname, email=email, phone=phone)

        form.save()
        return redirect('/')
    return render(request, 'page/create.html')

def add(request):
    form = addform()
    if request.method == 'POST':
        form = addform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = addform()
            

    return render(request, 'page/add.html',{'form':form})

def profile(request,id):
    customer = customers.objects.get(id=id)
    return render(request, 'page/profile.html', {'customer':customer})

def delete(request,id):
    customer = customers.objects.get(id=id)
    customer.delete()
    return redirect('/')

def edit(request,id):
    customer = customers.objects.get(id=id)
    form = addform(instance = customer)

    if request.method == 'POST':
        form = addform(request.POST, instance = customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'page/edit.html', {'form': form, 'customer': customer})


