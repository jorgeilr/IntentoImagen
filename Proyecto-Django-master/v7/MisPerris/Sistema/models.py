from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #Agregamos datos
    perfil=models.CharField(max_length=20,default="Usuario")
    rut=models.CharField(max_length=15,primary_key=True)
    nombre=models.CharField(max_length=100,blank=False,null=False)
    #fechaNacimiento=models.DateField(blank=True,null=True)
    #telefono=models.IntegerField(blank=False,null=False)
    #region=models.CharField(max_length=20,default="Metropolitana")
    #ciudad=models.CharField(max_length=20,default="Santiago")
    #tipoHogar=models.CharField(max_length=20,default="Departamento")
class Mascota(models.Model):
    fichaMascota=models.AutoField(primary_key=True)
    fotoMascota=models.ImageField(upload_to='./media/')
    nombreMascota=models.CharField(max_length=50 ,blank=False,null=False)
    razaMascota=models.CharField(max_length=50,blank=False,null=False)
    descripcion=models.CharField(max_length=255)
    estadoMascota=models.CharField(max_length=30,default="Rescatado")
