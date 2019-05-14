from django.forms import ModelForm
from .models import  Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields =[ 'NOME_CLI', 'CPF_CNPJ_CLI','EML_CLI','STA_CLI',]