from django.db import models

# Create your models here.
class Libro(models.Model):
  idLibro = models.IntegerField(verbose_name='IdLibro')
  codigo = models.IntegerField(verbose_name='Código')
  titulo = models.CharField(max_length=100, verbose_name='Título')
  isbn = models.CharField(max_length=30, verbose_name='ISBN')
  numpags = models.IntegerField(verbose_name='NumPags')
   
  class Meta:
    verbose_name_plural = 'Libros'
    
  def __str__(self):
    return self.titulo

class Autor(models.Model):
  idautor = models.IntegerField(verbose_name="IdAutor")
  idlibro = models.ForeignKey(Libro, on_delete=models.CASCADE)
  nombre = models.CharField(max_length=100, verbose_name="Nombre")
  nacionalidad = models.CharField(max_length=50, verbose_name="Nacionalidad")
  
  class Meta:
    verbose_name_plural = 'Autores'
    
  def __str__(self):
    return self.nombre

class Usuario(models.Model):
  idusuario = models.IntegerField(verbose_name="IdUsuario")
  numusuario = models.IntegerField(verbose_name="NumUsuario")
  nif = models.CharField(max_length=20, verbose_name="NIF")
  nombre = models.CharField(max_length=100, verbose_name="Nombre")
  direccion = models.CharField(max_length=255, verbose_name="Dirección")
  telefono = models.CharField(max_length=20, verbose_name="Teléfono")
  
  class Meta:
    verbose_name_plural = 'Usuarios'
    
  def __str__(self):
    return self.nombre

class Prestamos(models.Model):
  idprestamo = models.IntegerField(verbose_name="IdPrestamo")
  idlibro = models.ForeignKey(Libro, on_delete=models.CASCADE)
  idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  fecprestamo = models.DateField(auto_now=True)
  fecdevolucion = models.DateField()
  
  class Meta:
    verbose_name_plural = 'Prestamos'
    