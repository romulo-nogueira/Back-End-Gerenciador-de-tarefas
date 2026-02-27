from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Conecta as suas rotas da app tasks no caminho /api/
    path('api/', include('tasks.urls')), 
]