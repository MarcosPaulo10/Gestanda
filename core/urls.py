from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastros/', include('cadastro.urls')),
    path('contas/', include('contas.urls')),
]
