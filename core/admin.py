from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Despesas

class DespesasAdmin(admin.ModelAdmin):
    list_display = ('Descricao', 'Valor', 'Quitado')

admin.site.register(Despesas, DespesasAdmin)
