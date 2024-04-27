from django.db import models
import datetime
import bcrypt
# Create your models here.

class DateTimeModel(models.Model):
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

    class Meta:
        abstract = True

class Cliente(DateTimeModel):
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    correo = models.EmailField(null = True, blank = True, default = True)
    celular = models.IntegerField()
    password = models.CharField(max_length=255, null = True)
    
    def save(self, *args, **kwargs):
        if self.password:
            salt = bcrypt.gensalt()
            self.password = bcrypt.hashpw(self.password.encode('utf-8'), salt)
            super().save(*args, **kwargs)
    def __str__(self):
        return self.nombres
    
class Producto(DateTimeModel):
    nombre_producto = models.CharField(max_length=30)
    abreviatura = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=40)
    def __str__(self):
        return self.nombre_producto

class Cliente_Producto(DateTimeModel):
    id_cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, blank = False, null = False, default = 1)
    id_producto = models.ForeignKey(Producto, on_delete = models.CASCADE, blank = False, null = False, default = 1)
    numero_cuenta = models.IntegerField()
    def __str__(self):
        return self.id_cliente.id

class Tipo_Transaccion(DateTimeModel):
    nombre = models.CharField(max_length=20)
    abreviatura = models.CharField(max_length=3, null = False)
    descripcion = models.CharField(max_length=40)
    def __str__(self):
        return self.nombre    

class Transaccion(DateTimeModel):
    id_cliente_producto = models.ForeignKey(Cliente_Producto, on_delete = models.CASCADE, blank = False, null = False, default = 1)
    monto = models.IntegerField()
    tipo_transaccion = models.IntegerField()
    def __str__(self):
        return self.id_cliente_producto.id