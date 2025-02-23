from .models import (
TbCampanhas,
TbAsItem_Modelo, 
TbModelo_Cesta, 
TbItem_Cesta 
)
from datetime import datetime

def contabilizar_Cesta(FIDCesta: int):
    Cesta_Basica = {}
    Modelo_Itens = TbAsItem_Modelo.objects.filter(id_Cesta=FIDCesta)

    for modelo_Item in Modelo_Itens:
        ItemCesta = TbItem_Cesta.objects.get(ID_Item_Cesta=modelo_Item.ID_Item_Cesta.ID_Item_Cesta)
        MaxCestas = ItemCesta.Quant_Obtida // ItemCesta.Quant_padrao
        Cesta_Basica[ItemCesta.Nome] = [ItemCesta.ID_Item_Cesta, MaxCestas, ItemCesta.Quant_padrao]

    if Cesta_Basica:
        quant_Cestas = min(Cesta_Basica.values(), key=lambda x: x[1])[1]
    else:
        quant_Cestas = 0

    for Item in Cesta_Basica.values():
        Item_Cesta = TbItem_Cesta.objects.get(ID_Item_Cesta=Item[0])
        redutor = Item[2] * quant_Cestas
        Item_Cesta.Quant_Obtida -= redutor
        Item_Cesta.save()

    Modelo_Cesta = TbModelo_Cesta.objects.get(id_Cesta=FIDCesta)
    Modelo_Cesta.Quant_Arrecadadas += quant_Cestas
    Modelo_Cesta.save()

    return Modelo_Cesta.Quant_Arrecadadas

def analisar_metas(FIDCampanha: int):
    Campanha = TbCampanhas.objects.get(ID_Campanha=FIDCampanha)
    Modelo_Cesta = TbModelo_Cesta.objects.get(id_Cesta=Campanha.Id_Cesta.id_Cesta)
    
    contabilizar_Cesta(Modelo_Cesta.id_Cesta)  # Certifique-se que essa função está correta
    meta_cestas = Campanha.Quantidade_Cestas
    estoque_cestas = Modelo_Cesta.Quant_Arrecadadas

    if Campanha.Prazo < datetime.now().date():
        Campanha.status = 'atrasada'

    if estoque_cestas >= meta_cestas and Campanha.status != 'concluida':
        if Campanha.status == 'atrasada':
            Campanha.status = 'concluida com atraso'
        elif Campanha.status != 'concluida com atraso':
            Campanha.status = 'concluida'

        Modelo_Cesta.Quant_Arrecadadas = estoque_cestas - meta_cestas

    Modelo_Cesta.save()
    Campanha.save()

    return Campanha.status