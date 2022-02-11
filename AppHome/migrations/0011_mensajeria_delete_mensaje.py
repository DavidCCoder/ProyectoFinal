# Generated by Django 4.0 on 2022-02-10 22:32

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('AppHome', '0010_alter_post_subtitulo_alter_post_titulo_mensaje'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateTimeField(auto_now_add=True)),
                ('Asunto', models.CharField(max_length=60)),
                ('Mensaje', ckeditor.fields.RichTextField()),
                ('Autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Mensaje',
        ),
    ]
