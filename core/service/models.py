from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    last_name = models.CharField(max_length=50, verbose_name=_('Last Name'))
    email = models.EmailField(verbose_name=_('Email'))
    phone = models.CharField(max_length=12, verbose_name=_('Phone Number'))
    message = models.TextField(verbose_name=_('Message'))
    date = models.DateTimeField(auto_now_add=True, auto_created=True, verbose_name=_('Date'))

    def __str__(self):
        return self.email


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    email = models.EmailField(verbose_name=_('Email'), null=True, blank=True)
    phone = models.CharField(max_length=12, verbose_name=_('Phone Number'), null=True, blank=True)
    message = models.TextField(verbose_name=_('Message'))
    date = models.DateTimeField(auto_now_add=True, auto_created=True, verbose_name=_('Date'))

    def __str__(self):
        return self.email

class Service(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Service'))
    description = models.TextField(verbose_name=_('Description'))
    category = models.ForeignKey('ServiceCategory', on_delete=models.PROTECT, null=True,blank=True)
    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.name

class ServiceCategory(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('ServiceCategory'))

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.pk})

class Slider(models.Model):
    name = models.CharField(max_length=70, verbose_name=_('Slider'))
    description = models.TextField(verbose_name=_('Description'))
    def get_absolute_url(self):
        return reverse('slider_detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.name
