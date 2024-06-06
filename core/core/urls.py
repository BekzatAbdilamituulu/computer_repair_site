from django.contrib import admin
from django.urls import path, include
from service.views import *
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog
urlpatterns = [
    path('jet/', include('jet.urls'), name='jet'),
    path('admin/', admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]

urlpatterns += i18n_patterns(
    path('', include('service.urls')),
    )
