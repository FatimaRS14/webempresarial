from django.contrib import admin
from . models import Category, Post 
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    #La lista se tiene que dejar al final con una , si es que solo se implementara un campo 
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    #Implementación del formulario de busqueda
    #Se tiene que poner doble _ para dar la especificación de lo que se buscara
    date_hierarchy = 'published'
    #Gestión de la busqueda por saltos de fecha
    list_filter = ('author__username', 'categories__name')
    #Creación de campos manualmente
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description = "Categorias"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)