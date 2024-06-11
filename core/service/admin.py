from django.contrib import admin
from .models import Contact, Service, Slider, ServiceCategory, Client
from modeltranslation.admin import TranslationAdmin

class ServiceAdmin(TranslationAdmin):
	pass
class SliderAdmin(TranslationAdmin):
	pass
class ServiceCategoryAdmin(TranslationAdmin):
	pass

admin.site.register(Contact)
admin.site.register(Client)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
# Register your models here.
