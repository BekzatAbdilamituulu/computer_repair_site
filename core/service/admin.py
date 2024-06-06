from django.contrib import admin
from .models import Contact, Service, Slider
from modeltranslation.admin import TranslationAdmin

class ServiceAdmin(TranslationAdmin):
	pass
class SliderAdmin(TranslationAdmin):
	pass

admin.site.register(Contact)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Slider, SliderAdmin)

# Register your models here.
