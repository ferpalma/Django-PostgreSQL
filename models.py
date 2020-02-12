from django.db import models

# Create your models here.

class Pessoa(models.Model):

    nome = models.CharField(max_length=60)

class Fornecedor_credor(Pessoa):

    validar_cpf_cnpj = models.BooleanField()
    cpf_cnpj = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Empresa_software(Pessoa):

    def __str__(self):
        return self.nome

class Municipio(Pessoa):

    url_dados = models.CharField(max_length=150)
    id_empresa_software = models.ForeignKey(Empresa_software, verbose_name='Empresa_software', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Classificacao_orcamentaria(models.Model):

    numero = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    subfuncao = models.CharField(max_length=100)
    unidade_orcamentaria = models.CharField(max_length=100)
    natureza = models.CharField(max_length=100)
    fonte = models.CharField(max_length=100)
    
    def __str__(self):
        return self.numero
    
class Empenho(models.Model):
    
    dt_emissao = models.DateField()
    dt_create = models.DateTimeField()
    numero = models.CharField(max_length=60)
    valor = models.FloatField()
    id_municipio = models.ForeignKey(Municipio, verbose_name='Municipio', on_delete=models.CASCADE)
    servico_produto = models.CharField(max_length=60)
    id_classificacao_orcamentaria = models.ForeignKey(Classificacao_orcamentaria, verbose_name='Classificacao_orcamentaria', on_delete=models.CASCADE)
    id_fornecedor_credor = models.ForeignKey(Fornecedor_credor, verbose_name='Fornecedor_credor', on_delete=models.CASCADE)

    def __str__(self):
        return self.numero
 