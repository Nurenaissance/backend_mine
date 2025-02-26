# Generated by Django 4.1 on 2024-08-12 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0001_initial'),
        ('custom_fields', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customfield',
            name='tenant_id',
        ),
        migrations.RemoveField(
            model_name='customfield',
            name='user_id',
        ),
        migrations.AddField(
            model_name='customfield',
            name='tenant',
            field=models.ForeignKey(default='ll', on_delete=django.db.models.deletion.CASCADE, to='tenant.tenant'),
        ),
        migrations.AlterField(
            model_name='customfield',
            name='model_name',
            field=models.CharField(choices=[('account', 'Account'), ('calls', 'calls'), ('lead', 'Lead'), ('interaction', 'Interaction'), ('contact', 'Contact'), ('product', 'Product'), ('vendors', 'Vendors')], max_length=20),
        ),
    ]
