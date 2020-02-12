from django.contrib import admin
from .models import Empenho, Fornecedor_credor, Municipio, Empresa_software, Classificacao_orcamentaria

# Register your models here.

admin.site.register(Fornecedor_credor)
admin.site.register(Municipio)
admin.site.register(Empresa_software)
admin.site.register(Classificacao_orcamentaria)
admin.site.register(Empenho)