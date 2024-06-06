from django.contrib import admin
from django.urls import path, include
from service.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('slider_detail/<int:pk>/', SliderDetailView.as_view(), name='slider_detail'),
    path('service_detail/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('why/', why, name='why'),
    path('qa/', qa, name='qa'),
    path('contact/', ContactView.as_view(), name='contact'),
]
