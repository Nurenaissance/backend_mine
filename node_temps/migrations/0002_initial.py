# Generated by Django 4.1 on 2024-06-14 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("node_temps", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="nodetemplate",
            name="createdBy",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="node_temp_createdby",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
