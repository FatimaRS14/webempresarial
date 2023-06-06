from django.contrib import admin
from .models import Link
# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


    #Esto es para que se de la validacion al tipo de usuario y asi pueda tener diferencias al modificacr
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists():
            return('created', 'updated', 'Key', 'name')
        else:
            return ('created', 'updated')

admin.site.register(Link, LinkAdmin)