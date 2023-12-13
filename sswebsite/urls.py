from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import dashboard, delete_certificate

urlpatterns = [
    path('', views.home, name = 'home'),
    path('dashboard', views.dashboard, name= 'dashboard'),
    path('upload_certificate', views.upload_certificate, name= 'upload_certificate'),
    path('delete_certificate/<int:certificate_id>/', delete_certificate, name='delete_certificate'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)