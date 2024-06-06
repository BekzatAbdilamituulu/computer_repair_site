from modeltranslation.translator import translator, TranslationOptions
from .models import Service, Slider

class ServiceTranslationOptions(TranslationOptions):
	fields = ('name', 'description')

translator.register(Service, ServiceTranslationOptions)

class SliderTranslationOptions(TranslationOptions):
	fields = ('name', 'description')

translator.register(Slider, SliderTranslationOptions)