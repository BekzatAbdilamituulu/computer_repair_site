from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ContactForm, ClientForm
from django.views.generic import View, DetailView, ListView
from .models import Contact
from django.contrib import messages
from django.utils.translation import gettext as _
from .models import *


class HomeView(View):
    context = {}
    def get(self, request):
        self.context['slider'] = Slider.objects.all()
        self.context['service'] = Service.objects.all()
        self.context['category'] = ServiceCategory.objects.all()
        form = ContactForm()
        self.context['form'] = form
        return render(request, 'base.html', self.context)
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your message has been submitted successfully!'))

        self.context['form'] = form
        self.context['detail'] = Contact.objects.all()
        
class SliderDetailView(DetailView):
    model = Slider
    template_name = 'slider_detail.html'  # Customize this template

    def get_object(self, queryset=None):
        # Retrieve the slider based on the slug (or any other unique identifier)
        return Slider.objects.get(pk=self.kwargs['pk'])

def about(request):
    return render(request,'about.html')

class ContactView(View):
    context = {}
    def get(self, request):
        form = ContactForm()
        self.context['form'] = form
        return render(request, 'contact.html', self.context)
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your message has been submitted successfully!'))

        self.context['form'] = form
        self.context['detail'] = Contact.objects.all()
        return render(request, 'contact.html', self.context)
def service(request):
    service = Service.objects.all()
    context = {
    'service': service,
    }
    return render(request, 'service.html', context)

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_detail.html'  # Customize this template

    def get_object(self, queryset=None):
        # Retrieve the slider based on the slug (or any other unique identifier)
        return Service.objects.get(pk=self.kwargs['pk'])

def category_detail(request, pk):
    cat = ServiceCategory.objects.get(id=pk)
    service = Service.objects.filter(category_id__exact=cat)

    return render (request, 'servicecategory_list.html', {'cat': cat, 'service': service})

class WhyView(View):
    context = {}
    def get(self, request):
        form = ContactForm()
        self.context['form'] = form
        return render(request, 'why.html', self.context)
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your message has been submitted successfully!'))

        self.context['form'] = form
        self.context['detail'] = Contact.objects.all()
        return render(request, 'why.html', self.context)

class ClientView(View):
    context = {}
    def get(self, request):
        form = ClientForm()
        self.context['form'] = form
        return render(request, 'client.html', self.context)
    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your message has been submitted successfully!'))

        self.context['form'] = form
        self.context['detail'] = Client.objects.all()
        return render(request, 'client.html', self.context)


def service(request):
    service = Service.objects.all()
    context = {
    'service': service,
    }
    return render(request, 'service.html', context)
    return render(request,'why.html')

def qa(request):
    return render(request,'qa.html')


# some