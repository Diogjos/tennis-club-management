from django.contrib import admin
from .models import Membros
# Register your models here.

class MembrosAdmin (admin.ModelAdmin):
    list_display = ("nome", "sobrenome", "dataEntrada", )

admin.site.register(Membros, MembrosAdmin)