from django.shortcuts import render
from .models import *
# Create your views here.
def hi(request):
    return render(request,"app/index.html")
def about(request):
    return render(request,"app/about.html")
def contactus(request):
    return render(request,"app/contactus.html")
def Insertdata(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    Contact = request.POST['contact']

    newuser = contact.objects.create(
        firstname=firstname, lastname=lastname, Email=email, Contact=Contact)
    return render(request,'app/suc.html')


def services(request):
    return render(request,"app/services.html")
def reg(request):
    return render(request,"app/regforn.html")
def data(request):
    name = request.POST['name']
    email = request.POST['email']
    gender = request.POST['gender']
    age = request.POST['age']
    box = request.POST['Health_Issues']
    number = request.POST['number']
    add = request.POST['add']
    sd = request.POST["sd"]
    if sd =="Andrew":
        newuser = texasapp.objects.create(
            name=name, email=email, gender=gender, age=age, Health_Issues=box, number=number, add=add, sd=sd)
        return render(request, "app/slot.html")
    elif sd=="Senthil":
        newuser = texasapp.objects.create(
            name=name, email=email, gender=gender, age=age, Health_Issues=box, number=number, add=add, sd=sd)
        return render(request, "app/senthil.html")
    elif sd =="Afsal":
        newuser = texasapp.objects.create(
            name=name, email=email, gender=gender, age=age, Health_Issues=box, number=number, add=add, sd=sd)
        return render(request, "app/afsal.html")
    elif sd =="Vikram":
        newuser = texasapp.objects.create(
            name=name, email=email, gender=gender, age=age, Health_Issues=box, number=number, add=add, sd=sd)
        return render(request, "app/vikram.html")

def andrew(request):
    if request.method == "POST":
        namea = request.POST["name"]
    data = Andrew_Booking.objects.create(NAME1=namea)
    return render(request,"app/suc.html")
def Senthil(request):
    if request.method == "POST":
        namea = request.POST["name"]
    data = Senthil_Booking.objects.create(NAME1=namea)
    return render(request, "app/suc.html")
def afsalas(request):
    if request.method == "POST":
        namea = request.POST["name"]
    data = afsalas_Booking.objects.create(NAME1=namea)
    return render(request, "app/suc.html")
def vikramas(request):
    if request.method == "POST":
        namea = request.POST["name"]
    data = vikram_Booking.objects.create(NAME1=namea)
    return render(request, "app/suc.html")
