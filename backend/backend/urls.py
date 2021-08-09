from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers
from projects import views

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectView, 'project')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include('router.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
