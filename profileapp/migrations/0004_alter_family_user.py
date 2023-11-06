# Generated by Django 4.2.7 on 2023-11-06 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profileapp', '0003_alter_family_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='family', to=settings.AUTH_USER_MODEL),
        ),
    ]
