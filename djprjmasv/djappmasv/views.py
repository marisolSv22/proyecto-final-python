from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.views import View
from djappmasv.utils import render_to_pdf

from django.core.files.storage import FileSystemStorage

# Para pdf:
from django.template.loader import get_template
from io import BytesIO
from django.http import HttpResponse
import xhtml2pdf as pisa
import os
from random import randint

from django.views.generic.edit import UpdateView
from django.views.generic import ListView, CreateView, DeleteView 
from django.urls import reverse

from djappmasv.models import  TblLibros, TblCategorias, TblAutores, TblClientes, TblPedidoCliente, TblLibroPorAutor, TblUsuarios, AuthUser
from djappmasv.forms import FormularioLibros_masv, FormularioAutores_masv, FormularioClientes_masv, FormularioCategorias_masv, FormularioPedidoCliente_masv, FormularioLibroPorAutor_masv, FormularioUsuarios_masv


# Create your views here.

def index(request):
    return render(request, 'djappmasv/index.html')

def login(request):
    return render(request, 'djappmasv/login.html')

def error(request):
    return render(request, 'djappmasv/error.html')

#------------------------ Clientes --------------------------------  

class ClientesList_masv(ListView):
    model = TblClientes
    template_name = 'djappmasv/clientes/listar_clientes.html'

    def get_queryset(self):
        return TblClientes.objects.filter(estado='ACTIVO')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(ClientesList_masv,self).dispatch(request,*args, **kwargs)     

class ClientesAdd_masv(CreateView):
        model =  TblClientes
        form_class = FormularioClientes_masv
        template_name = 'djappmasv/clientes/insertar_clientes.html'

        def get_success_url(self):
            return reverse('clientes')

class ClientesUpd_masv(UpdateView):
    model = TblClientes
    form_class = FormularioClientes_masv
    template_name = 'djappmasv/clientes/editar_clientes.html'
    def get_success_url(self):
        return reverse('clientes')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(ClientesUpd_masv,self).dispatch(request,*args, **kwargs)

class ClientesDel_masv(DeleteView):
        model = TblClientes
        template_name = 'djappmasv/clientes/eliminar_clientes.html'
        def get_success_url(self):
            return reverse('clientes')

class ClienteReport_masv(View):
    def get(self, request, *args, **kwargs):
        object_list = TblClientes.objects.all()
        data = {
            'object_list': object_list
        }
        pdf = render_to_pdf('djappmasv/clientes/pdf_clientes.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(ClienteReport_masv,self).dispatch(request,*args,**kwargs)

# ------------------------------- Autores -------------------------

class AutoresList_masv(ListView):
    model = TblAutores
    template_name = 'djappmasv/autores/listar_autor.html'

    def get_queryset(self):
        return TblAutores.objects.filter(estado='ACTIVO')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(AutoresList_masv,self).dispatch(request,*args, **kwargs)

class AutoresAdd_masv(CreateView):
    model =  TblAutores
    form_class = FormularioAutores_masv
    template_name = 'djappmasv/autores/insertar_autor.html'
    def get_success_url(self):
        return reverse('autores')

class AutoresUpd_masv(UpdateView):
    model =  TblAutores
    form_class = FormularioAutores_masv
    template_name = 'djappmasv/autores/editar_autor.html'
    def get_success_url(self):
        return reverse('autores')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(AutoresUpd_masv,self).dispatch(request,*args, **kwargs)

class AutoresDel_masv(DeleteView):
    model =  TblAutores
    template_name = 'djappmasv/autores/eliminar_autor.html'
    def get_success_url(self):
        return reverse('autores')

class AutoresReport_masv(View):
    def get(self, request, *args, **kwargs):
        object_list = TblAutores.objects.all()
        data = {
            'object_list': object_list
        }
        pdf = render_to_pdf('djappmasv/autores/pdf_autor.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(AutoresReport_masv,self).dispatch(request,*args,**kwargs)

# ------------------------------- Categorias -------------------------

class CategoriasList_masv(ListView):
    model = TblCategorias
    template_name = 'djappmasv/categorias/listar_categorias.html'

    def get_queryset(self):
        return TblCategorias.objects.filter(estado='ACTIVO')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(CategoriasList_masv,self).dispatch(request,*args, **kwargs)

class CategoriasAdd_masv(CreateView):
    model =  TblCategorias
    form_class = FormularioCategorias_masv
    template_name = 'djappmasv/categorias/insertar_categorias.html'
    def get_success_url(self):
        return reverse('categoria')

class CategoriasUpd_masv(UpdateView):
    model =  TblCategorias
    form_class = FormularioCategorias_masv
    template_name = 'djappmasv/categorias/editar_categorias.html'
    def get_success_url(self):
        return reverse('categoria')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(CategoriasUpd_masv,self).dispatch(request,*args, **kwargs)

class CategoriasDel_masv(DeleteView):
    model =  TblCategorias
    template_name = 'djappmasv/categorias/eliminar_categorias.html'
    def get_success_url(self):
        return reverse('categoria')

class CategoriaReport_masv(View):
    def get(self, request, *args, **kwargs):
        object_list = TblCategorias.objects.all()
        data = {
            'object_list': object_list
        }
        pdf = render_to_pdf('djappmasv/categorias/pdf_cat.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(CategoriaReport_masv,self).dispatch(request,*args,**kwargs)

#-------------------------- Libros -----------------------------

class LibrosList_masv(ListView):
    model = TblLibros
    template_name = 'djappmasv/libros/listar_libros.html'

    def get_queryset(self):
        return TblLibros.objects.filter(estado='ACTIVO')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(LibrosList_masv,self).dispatch(request,*args, **kwargs)

class LibrosAdd_masv(CreateView):
    model =  TblLibros
    form_class = FormularioLibros_masv
    template_name = 'djappmasv/libros/insertar_libros.html'

    try:
        foto_p = request.FILES['portada']
        ruta_foto = f"media/{foto_p.name}"
        fs = FileSystemStorage()
        file_name = fs.save(foto_p.name, foto_p)
    except:
        ruta_foto = "media/no_imagen.png"

    def get_success_url(self):
        return reverse('libros')

class LibrosUpd_masv(UpdateView):
    model =  TblLibros
    form_class = FormularioLibros_masv
    template_name = 'djappmasv/libros/editar_libros.html'

    def get_success_url(self):
        return reverse('libros')

    try:
        foto_p = request.FILES['portada']
        ruta_foto = f"media/{foto_p.name}"
        fs = FileSystemStorage()
        file_name = fs.save(foto_p.name, foto_p)
    except:
        ruta_foto = "media/no_imagen.png"

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(LibrosUpd_masv,self).dispatch(request,*args, **kwargs)

class LibrosDel_masv(DeleteView):
    model =  TblLibros
    template_name = 'djappmasv/libros/eliminar_libros.html'
    def get_success_url(self):
        return reverse('libros')

class LibroReport_masv(View):
    def get(self, request, *args, **kwargs):
        object_list = TblLibros.objects.all()
        data = {
            'object_list': object_list
        }
        pdf = render_to_pdf('djappmasv/libros/pdf_libros.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(LibroReport_masv,self).dispatch(request,*args,**kwargs)

#-------------------------- PedidoCliente -----------------------------

class PedidoClienteList_masv(ListView):
    model = TblPedidoCliente
    template_name = 'djappmasv/pedido_cliente/listar_pedidos.html'

    def get_queryset(self):
        return TblPedidoCliente.objects.filter(estado='ACTIVO')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(PedidoClienteList_masv,self).dispatch(request,*args, **kwargs)

class PedidoClienteAdd_masv(CreateView):
    model =  TblPedidoCliente
    form_class = FormularioPedidoCliente_masv
    template_name = 'djappmasv/pedido_cliente/insertar_pedidos.html'
    def get_success_url(self):
        return reverse('pedido')

class PedidoClienteUpd_masv(UpdateView):
    model =  TblPedidoCliente
    form_class = FormularioPedidoCliente_masv
    template_name = 'djappmasv/pedido_cliente/editar_pedidos.html'
    def get_success_url(self):
        return reverse('pedido')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(PedidoClienteUpd_masv,self).dispatch(request,*args, **kwargs)

class PedidoClienteDel_masv(DeleteView):
    model =  TblPedidoCliente
    template_name = 'djappmasv/pedido_cliente/eliminar_pedidos.html'
    def get_success_url(self):
        return reverse('pedido')

class PedidoClienteReport_masv(View):
    def get(self, request, *args, **kwargs):
        object_list = TblPedidoCliente.objects.all()
        data = {
            'object_list': object_list
        }
        pdf = render_to_pdf('djappmasv/pedido_cliente/pdf_pedidos.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(PedidoClienteReport_masv,self).dispatch(request,*args,**kwargs)

#-------------------------- Libro Por Autor -----------------------------

class LibroPorAutorList_masv(ListView):
    model = TblLibroPorAutor
    template_name = 'djappmasv/libro_por_autor/listar_lib.html'

    def get_queryset(self):
        return TblLibroPorAutor.objects.filter(estado='ACTIVO')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(LibroPorAutorList_masv,self).dispatch(request,*args, **kwargs)

class LibroPorAutorAdd_masv(CreateView):
    model =  TblLibroPorAutor
    form_class = FormularioLibroPorAutor_masv
    template_name = 'djappmasv/libro_por_autor/insertar_lib.html'
    def get_success_url(self):
        return reverse('libroporautor')

class libroPorAutorUpd_masv(UpdateView):
    model =  TblLibroPorAutor
    form_class = FormularioLibroPorAutor_masv
    template_name = 'djappmasv/libro_por_autor/editar_lib.html'
    def get_success_url(self):
        return reverse('libroporautor')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(libroPorAutorUpd_masv,self).dispatch(request,*args, **kwargs)

class LibroPorAutorDel_masv(DeleteView):
    model =  TblLibroPorAutor
    template_name = 'djappmasv/libro_por_autor/eliminar_lib.html'
    def get_success_url(self):
        return reverse('libroporautor')

class LibroPorAutorReport_masv(View):
    def get(self, request, *args, **kwargs):
        object_list = TblLibroPorAutor.objects.all()
        data = {
            'object_list': object_list
        }
        pdf = render_to_pdf('djappmasv/libro_por_autor/pdf_lpa.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(LibroPorAutorReport_masv,self).dispatch(request,*args,**kwargs)
    
#-------------------------- Usuarios -----------------------------

class UsuariosList_masv(ListView):
    model = TblUsuarios
    template_name = 'djappmasv/usuarios/listar_usu.html'

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(UsuariosList_masv,self).dispatch(request,*args, **kwargs)

class UsuariosAdd_masv(CreateView):
    model = TblUsuarios
    form_class = FormularioUsuarios_masv
    template_name = 'djappmasv/usuarios/insertar_usu.html'
    def get_success_url(self):
        return reverse('usuario')

class UsuariosUpd_masv(UpdateView):
    model =  TblUsuarios
    form_class = FormularioUsuarios_masv
    template_name = 'djappmasv/usuarios/editar_usu.html'
    def get_success_url(self):
        return reverse('usuario')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(UsuariosUpd_masv,self).dispatch(request,*args, **kwargs)

class UsuariosDel_masv(DeleteView):
    model =  TblUsuarios
    template_name = 'djappmasv/usuarios/eliminar_usu.html'
    def get_success_url(self):
        return reverse('usuario')

class UsuarioReport_masv(View):
    def get(self, request, *args, **kwargs):
        object_list = TblUsuarios.objects.all()
        data = {
            'object_list': object_list
        }
        pdf = render_to_pdf('djappmasv/usuarios/pdf_usu.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(UsuarioReport_masv,self).dispatch(request,*args,**kwargs)

    # INICIO SESION

def inicio_sesion(request):
    if request.POST:
        usuario = request.POST['usuario']
        clave = request.POST['password']

        try:
            #authUser = authUser.objects.get(username=usuario, password=clave)
            user = auth.authenticate(username = usuario, password = clave)
            auth.login(request, user)

            # return HttpResponse(f"Ingreso al inicio de sesion con el usuario: {usuario}")
        except (AuthUser.DoesNotExist, AttributeError):
            return HttpResponse("Error al intentar ingresar a la página")

        return redirect(login)
    else:
        return HttpResponse("Usted esta intentando ingresar incorrectamente...")

    #CERRAR SESION

def cerrar_sesion(request):
    auth.logout(request)

    return redirect(login)

