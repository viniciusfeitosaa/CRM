from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clientes.urls')),  # URL inicial configurada para a app 'clientes'
]
