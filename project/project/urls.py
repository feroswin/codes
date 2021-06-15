from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from firstapp import views
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("firstapp.urls")),
    path("about/", views.about),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
