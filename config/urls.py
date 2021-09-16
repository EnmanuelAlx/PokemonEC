from django.conf import settings
from django.urls import include, path
from django.contrib import admin

def hola(request):
    print('Hola mundo')

urlpatterns = [
    
    path(settings.ADMIN_URL, admin.site.urls),
    
    
]