from django import forms
from .models import TbModelo_Cesta

class ModeloCestaForm(forms.ModelForm):
    class Meta:
        model = TbModelo_Cesta
        fields = ["nome"]
        labels = {
            "nome": "Nome da Cesta",

        }
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),

        }
