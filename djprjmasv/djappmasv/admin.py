from django.contrib import admin
from djappmasv import models

admin.site.register(models.TblClientes)
admin.site.register(models.TblUsuarios)
admin.site.register(models.TblAutores)
admin.site.register(models.TblLibroPorAutor)
admin.site.register(models.TblLibros)
admin.site.register(models.TblCategorias)
admin.site.register(models.TblPedidoCliente)



