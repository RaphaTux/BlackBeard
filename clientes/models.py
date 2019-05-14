from django.db import models

# Model Clientes
class Cliente(models.Model):
    ID_CLIENTE   = models.IntegerField.primary_key = True
    ID_ENDERECO = models.IntegerField
    CPF_CNPJ_CLI = models.CharField(max_length=14)
    STA_CLI      = models.CharField(max_length=1)
    EML_CLI      = models.CharField(max_length=150)
    NOME_CLI     = models.CharField(max_length=300)
    CONTATO_CLI  = models.ExpressionList

    def __str__(self):
        return self.NOME_CLI




