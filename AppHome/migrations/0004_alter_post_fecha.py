# Generated by Django 4.0.1 on 2022-02-03 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppHome', '0003_alter_post_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
