from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TbItem_Cesta(models.Model):
    ID_Item_Cesta = models.AutoField(primary_key= True, null= False)
    Nome = models.CharField(max_length = 255, null= False)
    Quant_padrao = models.PositiveIntegerField(null= False)
    Quant_Obtida = models.PositiveIntegerField(null= False, default=0)

class TbModelo_Cesta(models.Model):
    id_Cesta = models.AutoField(primary_key= True, null= False)
    nome = models.CharField(max_length = 255,null= False)
    Quant_Arrecadadas = models.PositiveIntegerField(null= False, default=0)
    Quant_doadas = models.PositiveIntegerField(null= False, default=0)
    Item_e_cesta = models.ManyToManyField(TbItem_Cesta, through= "TbAsItem_Modelo")


class TbAsItem_Modelo(models.Model):
    ID_Item_Cesta = models.ForeignKey(TbItem_Cesta, on_delete=models.CASCADE)
    id_Cesta = models.ForeignKey(TbModelo_Cesta, on_delete=models.CASCADE)

class TbCampanhas(models.Model):
    ID_Campanha = models.AutoField(primary_key=True, null= False)
    Titulo = models.CharField(max_length= 255, null= False)
    Prazo = models.DateField(null= False)
    Quantidade_Cestas = models.PositiveIntegerField(null= False)
    STATUS_CHOICES = [
        ('em andamento', 'Em andamento'),
        ('concluida', 'Concluída'),
        ('atrasada', 'Atrasada'),
        ('concluida com atraso', 'Concluída com atraso'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='em andamento')
    Id_Cesta = models.ForeignKey(TbModelo_Cesta, verbose_name=("Modelo_cesta"), on_delete=models.CASCADE)

class TbDonation(models.Model):
    id_Donation = models.AutoField(primary_key= True, null= False)
    quantidade = models.PositiveIntegerField(null= False)
    Validade = models.DateField(null= False)
    confirmado = models.BooleanField(null= False, default= False)
    id_Item_Cesta= models.ForeignKey(TbItem_Cesta, verbose_name=("Item"), on_delete=models.CASCADE)
    id_User = models.ForeignKey(User, verbose_name=("Usuario"), on_delete=models.CASCADE)
