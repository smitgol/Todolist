# Generated by Django 3.1.6 on 2021-02-05 03:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0005_auto_20210204_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
