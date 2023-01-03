from dataclasses import fields
from pyexpat import model
from django import forms

from djappmasv.models import TblLibros, TblCategorias, TblUsuarios, TblClientes, TblAutores, TblLibroPorAutor, TblPedidoCliente

class FormularioClientes_masv(forms.ModelForm):

    class Meta:
        
        model=TblClientes                                                                              

        fields=[
            
            'id_cliente',
            'identificacion',
            'nombres',
            'apellidos',
            'telefono',
            'direccion',
            'correo_electronico',
            'estado'

        ]
    
        labels={
            
            'id_cliente':'Id_cliente',
            'identificacion':'Identificacion',
            'nombres':'Nombres',
            'apellidos':'Apellidos',
            'telefono':'Telefono',
            'direccion':'Direccion',
            'correo_electronico':'Correo_electronico',
            'estado':'Estado',
        }

        Widget={

            'id_cliente': forms.TextInput(attrs={'class':'form-control'}),
            'identificacion': forms.TextInput(attrs={'class':'form-control'}),
            'nombres': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'correo_electronico': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'value': 'ACTIVO', 'readonly':'true'}),
        }

class FormularioAutores_masv(forms.ModelForm):

    class Meta:
        
        model=TblAutores
        

        fields=[

            'nombres' ,
            'apellidos',
            'estado',

        ]
        
        labels={

            'nombres':'Nombres',
            'apellidos':'Apellidos',
            'estado':'Estado',
        }

        Widget={
            'nombres': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'value': 'ACTIVO', 'readonly':'true'}),
            
        }

class FormularioCategorias_masv(forms.ModelForm):

    class Meta:
        
        model=TblCategorias

        fields=[
            
            'id_categoria',
            'categoria',
            'estado'

        ]
        
        labels={
            
            'id_categoria':'Id_categoria',
            'categoria':'Categoria',
            'estado':'Estado',
        }

        Widget={

            'id_categoria': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'value': 'ACTIVO', 'readonly':'true'}),
        }

class FormularioLibros_masv(forms.ModelForm):
    class Meta:
        model = TblLibros

        fields = [
            'isbn',
            'titulo',
            'fecha_pub',
            'precio',
            'portada',
            'cantidad_stock',
            'estado',
            'categoria',
        ]
        labels = {

            'isbn': 'Isbn',
            'titulo': 'Titulo',
            'fecha_pub': 'Fecha_pub',
            'precio': 'Precio',
            'portada': 'Portada',
            'cantidad_stock': 'Cantidad_stock',
            'estado': 'Estado',
            'categoria': 'Categoria'
        }
        widgets = {
            
            'isbn': forms.TextInput(attrs={'class': 'form-control'}) ,
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_pub': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'portada': forms.FileInput(attrs = {'class':'form-control'}),
            'cantidad_stock': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'value': 'ACTIVO', 'readonly':'true'}),
            'categoria': forms.Select(attrs = {'class': 'form-select'}),
        }

class FormularioPedidoCliente_masv(forms.ModelForm):

    class Meta:
        
        model=TblPedidoCliente

        fields=[
            
            'id_pedido',
            'nro_pedido',
            'id_cliente',
            'isbn',
            'fecha_pedido',
            'cantidad',
            'subtotal',
            'estado'

        ]
        
        labels={
            
            'id_pedido':'Id_pedido',
            'nro_pedido':'Nro_pedido',
            'id_cliente':'Id_cliente',
            'isbn':'Isbn',
            'fecha_pedido':'Fecha_pedido',
            'cantidad':'Cantidad',
            'subtotal':'Subtotal',
            'estado':'Estado',
        }

        Widget={

            'id_pedido': forms.TextInput(attrs={'class':'form-control'}),
            'nro_pedido': forms.TextInput(attrs={'class':'form-control'}),
            'id_cliente': forms.Select(attrs = {'class': 'form-select'}),
            'isbn': forms.Select(attrs = {'class': 'form-select'}),
            'fecha_pedido': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad': forms.TextInput(attrs={'class':'form-control'}),
            'subtotal': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'value': 'ACTIVO', 'readonly':'true'}),
        }

class FormularioLibroPorAutor_masv(forms.ModelForm):

    class Meta:
        
        model=TblLibroPorAutor

        fields=[
            
            'id_autor',
            'isbn',
            'estado'

        ]
        
        labels={
            
            'id_autor':'Id_autor',
            'isbn':'Isbn',
            'estado':'Estado',
        }

        Widget={

            'id_autor': forms.Select(attrs = {'class': 'form-select'}),
            'isbn': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'value': 'ACTIVO', 'readonly':'true'}),
        }

class FormularioUsuarios_masv(forms.ModelForm):

    class Meta:
        
        model=TblUsuarios

        fields=[
            
            'id_usuario',
            'id_cliente',
            'usuario',
            'clave'

        ]
        
        labels={
            
            'id_usuario':'Id_usuario',
            'id_cliente':'Id_cliente',
            'usuario':'Usuario',
            'clave':'Clave'
        }

        Widget={

            'id_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'id_cliente': forms.TextInput(attrs={'class':'form-control'}),
            'usuario': forms.TextInput(attrs={'class':'form-control'}),
            'clave': forms.PasswordInput(attrs={'class':'form-control'}),
            
        }

