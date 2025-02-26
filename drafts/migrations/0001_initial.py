# Generated by Django 4.1 on 2024-07-24 06:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="drafts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image_url", models.URLField()),
                ("caption", models.TextField()),
                ("access_token", models.CharField(max_length=1200)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("is_story", models.BooleanField(default=False)),
                ("is_reel", models.BooleanField(default=False)),
                ("scheduled_date", models.DateField(blank=True, null=True)),
                ("scheduled_time", models.TimeField(blank=True, null=True)),
            ],
        ),
    ]
