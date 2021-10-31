# Generated by Django 3.2.8 on 2021-10-31 19:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(default=0, validators=[users.models.validate_age], verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='users/image_profile/default.png', upload_to=users.models._user_directory_path, verbose_name='profile photo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='phone number must not consist of space and requires country code. eg : +79546748973', regex='^\\+?1?\\d{9,15}$')], verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='region',
            field=models.CharField(max_length=50, verbose_name='region of residence'),
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ballance', models.PositiveIntegerField(default=0, verbose_name='user balance')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to=settings.AUTH_USER_MODEL, verbose_name='user`s wallet')),
            ],
            options={
                'permissions': (('can_add_money', 'top up balance'),),
                'unique_together': {('user', 'id')},
            },
        ),
    ]
