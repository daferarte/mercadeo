from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.CharField(max_length=255, verbose_name='Descripcion', blank=True)
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Creado')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre
    
class Plantilla(models.Model):
    titulo = models.CharField(max_length=150, verbose_name='Titulo')
    contenido = RichTextField(verbose_name='contenido')
    publicado = models.BooleanField(verbose_name="¿Publicado?")
    user = models.ForeignKey(User, editable=False, verbose_name="Usuario", on_delete=models.PROTECT)  
    Categoria = models.ManyToManyField(Categoria, verbose_name="categorías", blank=True)  # relacion de 1 a muchos un articulo puede tener muchas categorias
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    actualizado = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:
        verbose_name = 'Plantilla'
        verbose_name_plural = 'Plantillas'
        ordering = ['-creado']

    def __str__(self):
        return self.titulo

