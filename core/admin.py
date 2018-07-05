from django.contrib import admin
from .models import Prestador

# Register your models here.


class CoreAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Prestador, CoreAdmin)
