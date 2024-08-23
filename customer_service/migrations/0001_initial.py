# Generated by Django 4.2.11 on 2024-08-23 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=20, unique=True)),
                ('address', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('Installation', 'Installation'), ('Repair', 'Repair'), ('Maintenance', 'Maintenance')], max_length=20)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Submitted', 'Submitted'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')], default='Submitted', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attached_file', models.FileField(blank=True, null=True, upload_to='service_requests/')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_service.customer')),
            ],
        ),
    ]
