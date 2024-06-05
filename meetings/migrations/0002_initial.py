# Generated by Django 4.1 on 2024-06-04 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meetings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0002_initial'),
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetings',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='meeting_assigned_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meetings',
            name='contact_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meeting_contacts', to='contacts.contact', verbose_name='Contact Name'),
        ),
        migrations.AddField(
            model_name='meetings',
            name='createdBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meeting_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meetings',
            name='host',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='meeting_hosts', to=settings.AUTH_USER_MODEL, verbose_name='Host'),
        ),
        migrations.AddField(
            model_name='meetings',
            name='participants',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='meeting_participants', to='contacts.contact'),
        ),
        migrations.AddField(
            model_name='meetings',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant.tenant'),
        ),
    ]
