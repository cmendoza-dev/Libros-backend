from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Libro, Prestamos, Usuario, Autor
from .serializers import LibroSerializer, PrestamosSerializer, UsuarioSerializer, AutorSerializer
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.
# ViewSets define the view behavior.
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    parser_classes = (MultiPartParser, FormParser)

    
class PrestamosViewSet(viewsets.ModelViewSet):
    queryset = Prestamos.objects.all()
    serializer_class = PrestamosSerializer
    parser_classes = (MultiPartParser, FormParser)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    parser_classes = (MultiPartParser, FormParser)


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer    
    parser_classes = (MultiPartParser, FormParser)





