from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DeleteView

from . import models, forms


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
    method = request.method
    if method == "POST":
        contactForm = forms.Contact_form(request.POST, request.FILES)
        if contactForm.is_valid():
            contactForm.save()
            return redirect('/success')

    else:
        contactForm = forms.Contact_form()
    return render(request, "kontakten.html", {"contacts" : contacts,"contactForm": contactForm, "nav" : nav})

#Form page
def add_form(request):
    form_page = models.Form_page.objects.all()
    nav = models.Navbar.objects.all()
    method = request.method
    if method == "POST":
        form = forms.Form_registr(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/success')

    else:
        form = forms.Form_registr()
    return render(request, "form.html", {"form": form, "form_page": form_page, "nav": nav})

def success_form(request):
    form_page = models.Form_page.objects.all()
    return render(request, "success_Form.html", {"form_page": form_page})


#Form registrate data
class Data_forms(ListView):
    template_name = "data_registr.html"
    queryset = models.Form_registr.objects.all()

    def get_queryset(self):
        return models.Form_registr.objects.all()


#Contact Form data
class Contact_data(ListView):
    template_name = "contact_data.html"
    queryset = models.Contact_form.objects.all()

    def get_queryset(self):
        return models.Contact_form.objects.all()

#Deleting registrate
class DataDeleteViewRegistrate(DeleteView):
    template_name = "delete.html"
    success_url = "/data/"

    def get_object(self, **kwargs):
        data_id = self.kwargs.get("id")
        return get_object_or_404(models.Form_registr, id=data_id)

#Deleting contact
class DataDeleteViewContacts(DeleteView):
    template_name = "delete.html"
    success_url = "/contact-data/"

    def get_object(self, **kwargs):
        data_id = self.kwargs.get("id")
        return get_object_or_404(models.Contact_form, id=data_id)

