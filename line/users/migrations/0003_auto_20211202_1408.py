# Generated by Django 3.2.8 on 2021-12-02 14:08

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ('age',)},
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='amount')),
                ('descriptions', models.CharField(max_length=255, verbose_name='transaction description')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balance_changes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
