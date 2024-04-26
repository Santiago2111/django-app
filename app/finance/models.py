from django.db import models
#import datetime
# Create your models here.

#class DateTimeModel(models.Model):
    #created_at = models.DateTimeField(default=datetime.datetime.now())
    #updated_at = models.DateTimeField(default=datetime.datetime.now())
    #deleted_at = models.DateTimeField(null = True, blank = True)

    #class Meta:
        #abstract = True

class Cliente(models.Model):
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    correo = models.EmailField(null = True, blank = True, default = True)
    celular = models.IntegerField()
    def __str__(self):
        return self.correo
    
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=30)
    abreviatura = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=40)
    def __str__(self):
        return self.nombre_producto

class Cliente_Producto(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, blank = False, null = False, default = 1)
    id_producto = models.ForeignKey(Producto, on_delete = models.CASCADE, blank = False, null = False, default = 1)
    numero_cuenta = models.IntegerField()
    def __str__(self):
        return self.id_cliente

class Tipo_Transaccion(models.Model):
    nombre = models.CharField(max_length=20)
    abreviatura = models.CharField(max_length=3, null = False)
    descripcion = models.CharField(max_length=40)

class Transaccion(models.Model):
    id_cliente_producto = models.ForeignKey(Cliente_Producto, on_delete = models.CASCADE, blank = False, null = False, default = 1)
    monto = models.IntegerField()
    tipo_transaccion = models.IntegerField()