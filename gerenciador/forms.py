from django import forms
from .models import TbModelo_Cesta, TbCampanhas, TbItem_Cesta, TbAsItem_Modelo, TbDonation

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
class ItemForm(forms.ModelForm):
    class Meta:
        model = TbItem_Cesta
        fields = ["Nome", "Quant_padrao"]
        labels = {
            "Nome": "nome do item",
            "Quant_padrao": "quantidade padrão"
        }
        widgets = {
            "Nome": forms.TextInput(attrs={"class": "form-control"}),
            "Quant_padrao":forms.NumberInput(attrs={"class": "form-control"})

        }

class CampanhaForm(forms.ModelForm):
    class Meta:
        model = TbCampanhas
        fields = ["Titulo", "Prazo", "Quantidade_Cestas", "Id_Cesta"]
        widgets = {
            "Prazo": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "Titulo": forms.TextInput(attrs={"class": "form-control"}),
            "Quantidade_Cestas": forms.NumberInput(attrs={"class": "form-control"}),
        }
    def __init__(self, *args, **kwargs):
        super(CampanhaForm, self).__init__(*args, **kwargs)
        self.fields['Id_Cesta'].queryset = TbModelo_Cesta.objects.all()
        self.fields['Id_Cesta'].label_from_instance = (
            lambda obj: f"{obj.nome} ({obj.Quant_Arrecadadas} arrecadadas)"
            )

class AddItemCestaForm(forms.Form):
        item = forms.ModelChoiceField(
            queryset=TbItem_Cesta.objects.all(),
            label="Escolha um item para adicionar",
            widget=forms.Select(attrs={"class": "form-control"}),
        )
        def __init__(self, *args, **kwargs):
            super(AddItemCestaForm, self).__init__(*args, **kwargs)
            self.fields['item'].label_from_instance = lambda obj: f"{obj.Nome}: {obj.Quant_padrao} (Obtidas: {obj.Quant_Obtida})"

class DonationForm(forms.ModelForm):
    class Meta:
        model = TbDonation
        fields = ['quantidade', 'Validade', 'confirmado', 'id_Item_Cesta']
        widgets = {
            'Validade': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super(DonationForm, self).__init__(*args, **kwargs)
        self.fields['id_Item_Cesta'].queryset = TbModelo_Cesta.objects.all()
        self.fields['id_Item_Cesta'].label_from_instance = (
            lambda obj: f"{obj.nome}"
            )