# Generated by Django 4.2 on 2023-04-28 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0002_menu'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.AlterModelOptions(
            name='menuitem',
            options={'verbose_name': 'Пункт меню MPTT', 'verbose_name_plural': 'Пункты меню MPTT'},
        ),
    ]
