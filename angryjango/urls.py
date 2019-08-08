
from django.contrib import admin
from django.urls import path, include


API_ROOT_URL = 'api/v1/'
urlpatterns = [
    path('admin/', admin.site.urls),
    path(API_ROOT_URL, include('apps.accounts.urls')),
]
