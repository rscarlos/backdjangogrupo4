# Generated by Django 3.1.3 on 2020-11-24 00:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioModel',
            fields=[
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('usuId', models.AutoField(db_column='usu_id', primary_key=True, serialize=False)),
                ('usuCorreo', models.EmailField(db_column='usu_correo', max_length=254, unique=True)),
                ('usuNombre', models.CharField(db_column='usu_nombre', max_length=50)),
                ('usuApellido', models.CharField(db_column='usu_apellido', max_length=50)),
                ('usuDni', models.CharField(db_column='usu_dni', max_length=50)),
                ('password', models.TextField(db_column='usu_pass')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login', models.DateTimeField(null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 't_usuario',
            },
            managers=[
                ('objects', user.models.ManejoUsuario()),
            ],
        ),
        migrations.CreateModel(
            name='DireccionModel',
            fields=[
                ('dirId', models.AutoField(db_column='dir_id', primary_key=True, serialize=False, unique=True)),
                ('dirDes', models.CharField(db_column='dir_des', max_length=200)),
                ('dirNum', models.CharField(db_column='dir_num', max_length=10)),
                ('dirPer', models.CharField(db_column='dir_per', max_length=50)),
                ('dirRef', models.CharField(db_column='dir_ref', max_length=100)),
                ('createAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('updateAt', models.DateTimeField(auto_now=True, db_column='updated_at')),
                ('usuId', models.ForeignKey(db_column='usu_id', on_delete=django.db.models.deletion.PROTECT, related_name='DireccionUsuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 't_direccion',
            },
        ),
    ]
