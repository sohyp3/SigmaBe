from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('accs.urls')),
    path('api/accounting/', include('accounting.urls')),
]
