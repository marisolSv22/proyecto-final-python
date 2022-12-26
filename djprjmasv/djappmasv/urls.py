from django.urls import path
from djappmasv import views
from djappmasv.views import LibrosList_masv, LibrosAdd_masv, LibrosUpd_masv, LibrosDel_masv, AutoresList_masv, AutoresAdd_masv, AutoresUpd_masv, AutoresDel_masv, ClientesList_masv, ClientesAdd_masv, ClientesUpd_masv, ClientesDel_masv, CategoriasList_masv, CategoriasAdd_masv, CategoriasUpd_masv, CategoriasDel_masv, PedidoClienteList_masv, PedidoClienteAdd_masv, PedidoClienteUpd_masv, PedidoClienteDel_masv, LibroPorAutorList_masv, LibroPorAutorAdd_masv, libroPorAutorUpd_masv, LibroPorAutorDel_masv, UsuariosList_masv, UsuariosAdd_masv, UsuariosUpd_masv, UsuariosDel_masv, UsuarioReport_masv, LibroPorAutorReport_masv, PedidoClienteReport_masv, LibroReport_masv, ClienteReport_masv, CategoriaReport_masv, AutoresReport_masv

urlpatterns=[
    path('', views.index, name='inicio'),
    path('login/', views.login, name='login'),
    path('inicio_sesion', views.inicio_sesion, name='inicio_sesion'),
    path('logout', views.cerrar_sesion, name='cerrar_sesion'),
    path('error', views.error, name = 'error'),
# ----------------------------------- Clientes---------------------------------
    path('clientes/', ClientesList_masv.as_view(), name='clientes'),
    path('addclientes/', ClientesAdd_masv.as_view(), name='insertar_clientes'),
    path('updclientes/<pk>', ClientesUpd_masv.as_view(), name='actualizar_clientes'),
    path('delclientes/<pk>', ClientesDel_masv.as_view(), name='eliminar_clientes'),
    path('generarpdfcl/', ClienteReport_masv.as_view(), name='generarpdfcl'),
#------------------------------------- Autores ----------------------------------
    path('autores/', AutoresList_masv.as_view(), name='autores'),
    path('addautor/', AutoresAdd_masv.as_view(), name='insertar_autor'),
    path('updautor/<pk>', AutoresUpd_masv.as_view(), name='actualizar_autor'),
    path('delautor/<pk>', AutoresDel_masv.as_view(), name='eliminar_autor'),
    path('generarpdfau/', AutoresReport_masv.as_view(), name='generarpdfau'),
#------------------------------------ Categorias --------------------------------
    path('categoria/', CategoriasList_masv.as_view(), name='categoria'),
    path('addcategoria/', CategoriasAdd_masv.as_view(), name='insertar_categoria'),
    path('updcategoria/<pk>', CategoriasUpd_masv.as_view(), name='actualizar_categoria'),
    path('delcategoria/<pk>', CategoriasDel_masv.as_view(), name='eliminar_categoria'),
    path('generarpdfc/', CategoriaReport_masv.as_view(), name='generarpdfc'),
# --------------------------------- libros ----------------------------------------
    path('libros/', LibrosList_masv.as_view(), name='libros'),
    path('addlibros/', LibrosAdd_masv.as_view(), name='insertar_libros'),
    path('updlibros/<pk>', LibrosUpd_masv.as_view(), name='actualizar_libros'),
    path('dellibros/<pk>', LibrosDel_masv.as_view(), name='eliminar_libros'),
    path('generarpdfl/', LibroReport_masv.as_view(), name='generarpdfl'),
# ------------------------------- PedidoCliente -------------------------------------
    path('pedido/', PedidoClienteList_masv.as_view(), name='pedido'),
    path('addpedido/', PedidoClienteAdd_masv.as_view(), name='insertar_pedido'),
    path('updpedido/<pk>', PedidoClienteUpd_masv.as_view(), name='actualizar_pedido'),
    path('delpedido/<pk>', PedidoClienteDel_masv.as_view(), name='eliminar_pedido'),
    path('generarpdfpc/', PedidoClienteReport_masv.as_view(), name='generarpdfpc'),
# ------------------------------- Libro Por Autor -------------------------------------
    path('libroporautor/', LibroPorAutorList_masv.as_view(), name='libroporautor'),
    path('addlib/', LibroPorAutorAdd_masv.as_view(), name='insertar_lib'),
    path('updlib/<pk>', libroPorAutorUpd_masv.as_view(), name='actualizar_lib'),
    path('dellib/<pk>', LibroPorAutorDel_masv.as_view(), name='eliminar_lib'),
    path('generarpdfpa/', LibroPorAutorReport_masv.as_view(), name='generarpdflpa'),
# ------------------------------- Usuario -------------------------------------
    path('usuario/', UsuariosList_masv.as_view(), name='usuario'),
    path('addusu/', UsuariosAdd_masv.as_view(), name='insertar_usuario'),
    path('updusu/<pk>', UsuariosUpd_masv.as_view(), name='actualizar_usuario'),
    path('delusu/<pk>', UsuariosDel_masv.as_view(), name='eliminar_usuario'),
    path('generarpdfusu/', UsuarioReport_masv.as_view(), name='generarpdfusu'),



]