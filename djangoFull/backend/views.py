from django.shortcuts import render
from . import models

# Create your views here.
#Main page
def main(request):
    main = models.Main.objects.all()
    card = models.Feedback.objects.all()
    nav = models.Navbar.objects.all()
    return render(request, "index.html", {"main": main, "card": card, "nav": nav})

#Ferienjob page
def ferienjob(request):
    ferienjob = models.Ferienjob.objects.all()
    nav = models.Navbar.objects.all()
    return render(request, "ferienjob.html", {"ferienjob": ferienjob, "nav": nav})

#Deutschkurs page
def course(request):
    course = models.Course.objects.all()
    nav = models.Navbar.objects.all()
    return render(request, "deutschkurs.html", {"course": course, "nav": nav})

#Contacts page
def contacts(request):
    contacts = models.Contacts.objects.all()
    nav = models.Navbar.objects.all()
    return render(request, "kontakten.html", {"contacts" : contacts, "nav" : nav})
