from django.contrib import admin
from .models import Categoria, Plantilla

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', )
    search_fields = ('nombre', 'descripcion')
    # list_filter=('visible',)
    list_display = ('nombre', 'creado')
    ordering = ('-creado', )

# clase ArticleAdmin sirve para ordenar los articulos
class PlantillaAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'creado', 'actualizado')
    search_fields = ('titulo', 'contenido', 'user__username', 'Categoria__nombre')
    list_filter = ('publicado', 'Categoria')
    list_display = ('titulo', 'publicado', 'creado', 'user')
    ordering = ('-creado', )

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Plantilla, PlantillaAdmin)