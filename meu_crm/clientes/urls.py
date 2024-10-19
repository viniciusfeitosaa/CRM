from django.urls import path
from .views import lista_clientes, registro, login_view, logout_view, home, dashboard

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),  # URL para o dashboard
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
