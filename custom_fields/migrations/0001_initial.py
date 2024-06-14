# Generated by Django 4.1 on 2024-06-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CustomField",
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
                (
                    "model_name",
                    models.CharField(
                        choices=[
                            ("account", "Account"),
                            ("calls", "calls"),
                            ("lead", "Lead"),
                            ("interaction", "Interaction"),
                            ("conatact", "Contact"),
                        ],
                        max_length=20,
                    ),
                ),
                ("custom_field", models.CharField(max_length=255)),
                ("value", models.TextField(blank=True, null=True)),
                (
                    "field_type",
                    models.CharField(
                        choices=[
                            ("char", "CharField"),
                            ("text", "TextField"),
                            ("int", "IntegerField"),
                            ("float", "FloatField"),
                            ("bool", "BooleanField"),
                            ("date", "DateField"),
                            ("datetime", "DateTimeField"),
                            ("email", "EmailField"),
                            ("url", "URLField"),
                        ],
                        max_length=20,
                    ),
                ),
                ("user_id", models.IntegerField(default=7)),
                ("tenant_id", models.IntegerField(default=3)),
                ("entity_id", models.IntegerField(default=1, editable=False)),
            ],
        ),
    ]
