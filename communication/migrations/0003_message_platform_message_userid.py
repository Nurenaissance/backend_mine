# Generated by Django 4.1 on 2024-08-07 07:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("communication", "0002_remove_message_conversation"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="platform",
            field=models.CharField(
                choices=[
                    ("whatsapp", "WhatsApp"),
                    ("instagram", "Instagram"),
                    ("email", "Email"),
                    ("call", "Call"),
                ],
                default="instagram",
                max_length=50,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="message",
            name="userid",
            field=models.CharField(
                default="aWdfZAG06MTpJR01lc3NhZA2VUaHJlYWQ6MTc4NDE0NjY0MDkwMzM0ODk6MzQwMjgyMzY2ODQxNzEwMzAxMjQ0Mjc2MDIwNDc4NzU3MzAwNjEx",
                max_length=5000,
            ),
            preserve_default=False,
        ),
    ]
