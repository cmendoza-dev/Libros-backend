from rest_framework import serializers
from .models import Libro, Prestamos, Usuario, Autor

class LibroSerializer(serializers.HyperlinkedModelSerializer):
    # imagen_url = serializers.ImageField(use_url=True, required=False)
    class Meta:
        model = Libro
        fields = '__all__'

class PrestamosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamos
        fields = '__all__'
        ordering = ["apellido"]

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'