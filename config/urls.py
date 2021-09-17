from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from django.conf.urls.static import static

urlpatterns = [
    
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include(('PokemonEC.evolution_chain_api.urls', 'api'), namespace='api')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)