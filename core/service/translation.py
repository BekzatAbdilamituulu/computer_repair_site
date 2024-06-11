from modeltranslation.translator import translator, TranslationOptions
from .models import Service, Slider, ServiceCategory

class ServiceTranslationOptions(TranslationOptions):
	fields = ('name', 'description')

translator.register(Service, ServiceTranslationOptions)

class SliderTranslationOptions(TranslationOptions):
	fields = ('name', 'description')

translator.register(Slider, SliderTranslationOptions)

class ServiceCategoryTranslationOptions(TranslationOptions):
	fields = ('name',)
translator.register(ServiceCategory, ServiceCategoryTranslationOptions)