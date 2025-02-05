from django.contrib import admin
from django.urls import path, include

from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('error/', generar_error, name='error'),
    path('onepage/',onepage,name='onepage'),
    path('prueba/',prueba, name="prueba"),
    path('busqueda/',busqueda, name="busqueda"),
    path('error_logs/', error_logs, name='error_logs'),
    path('api/error_logs/', get_error_logs, name='get_error_logs'),
    path('users/', include('users.urls')),
]