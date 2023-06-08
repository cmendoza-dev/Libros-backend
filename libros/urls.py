from django.urls import path, include
from rest_framework import routers
from .views import LibroViewSet, PrestamosViewSet, AutorViewSet, UsuarioViewSet


router = routers.DefaultRouter()
router.register(r'libros', LibroViewSet)
router.register(r'prestamos', PrestamosViewSet)
router.register(r'usuarios', AutorViewSet)
router.register(r'autores', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-libros/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-prestamos/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-usuarios/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-autores/', include('rest_framework.urls', namespace='rest_framework')),
] 
