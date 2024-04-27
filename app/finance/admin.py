from django.contrib import admin
from .models import Cliente, Producto, Cliente_Producto, Tipo_Transaccion, Transaccion

# Register your models here.

class ClientesFields(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'correo')

class TransaccionesFields(admin.ModelAdmin):
    list_display = ('id_cliente_producto', 'monto', 'tipo_transaccion')

admin.site.register(Cliente, ClientesFields)
admin.site.register(Producto)
admin.site.register(Cliente_Producto)
admin.site.register(Tipo_Transaccion)
admin.site.register(Transaccion)