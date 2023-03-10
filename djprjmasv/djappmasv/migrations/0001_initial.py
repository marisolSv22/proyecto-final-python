# Generated by Django 4.1.4 on 2022-12-22 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblAutores',
            fields=[
                ('id_autor', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=25)),
                ('apellidos', models.CharField(max_length=25)),
                ('estado', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'tbl_autores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblCategorias',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=40)),
                ('estado', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'tbl_categorias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblClientes',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('identificacion', models.CharField(max_length=11)),
                ('nombres', models.CharField(max_length=25)),
                ('apellidos', models.CharField(max_length=25)),
                ('telefono', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=100)),
                ('correo_electronico', models.EmailField(max_length=100)),
                ('estado', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'tbl_clientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblLibros',
            fields=[
                ('isbn', models.IntegerField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=125)),
                ('fecha_pub', models.DateField()),
                ('precio', models.IntegerField()),
                ('portada', models.FileField(blank=True, null=True, upload_to='media/')),
                ('cantidad_stock', models.CharField(max_length=125)),
                ('estado', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'tbl_libros',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblPedidoCliente',
            fields=[
                ('id_pedido', models.IntegerField(primary_key=True, serialize=False)),
                ('nro_pedido', models.IntegerField()),
                ('fecha_pedido', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('estado', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'tbl_pedido_cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblUsuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=128)),
                ('clave', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'tbl_usuarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblLibroPorAutor',
            fields=[
                ('id_autor', models.OneToOneField(db_column='id_autor', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='djappmasv.tblautores')),
                ('estado', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'tbl_libro_por_autor',
                'managed': False,
            },
        ),
    ]
