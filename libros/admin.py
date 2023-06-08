from django.contrib import admin

# Register your models here.
from .models import *

admin.site.site_header = 'BIBLIOTECA'
admin.site.index_title = 'Préstamo de libros'
admin.site.site_title = 'LIBRERIA || TECSUP'

class LibroAdmin(admin.ModelAdmin):
    # ...
    search_fields = ['titulo']
    icon_name = 'description'


admin.site.register(Libro, LibroAdmin)


class AutorAdmin(admin.ModelAdmin):
    # ...
    icon_name = 'group'

admin.site.register(Autor, AutorAdmin)

class PrestamosAdmin(admin.ModelAdmin):
    # ...
    icon_name = 'gamepad'

admin.site.register(Prestamos, PrestamosAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    # ...
    icon_name = 'account_box'

admin.site.register(Usuario, UsuarioAdmin)