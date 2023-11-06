# Generated by Django 4.2.7 on 2023-11-06 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articleapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newarticle',
            name='writer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='article_written', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
