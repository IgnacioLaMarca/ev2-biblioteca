from django.urls import path, include
from rest_framework import routers
from .views import LibroViewSet, MiembroViewSet, BibliotecaViewSet

router = routers.DefaultRouter()
router.register(r'libros', LibroViewSet)
router.register(r'miembros', MiembroViewSet)
router.register(r'biblioteca', BibliotecaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
