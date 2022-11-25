from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView
# contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
#    path('', contact, name='contact')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
