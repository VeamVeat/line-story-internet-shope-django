# Generated by Django 3.2.8 on 2021-11-23 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='slug',
        ),
    ]
