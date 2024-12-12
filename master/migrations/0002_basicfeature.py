# Generated by Django 3.2.18 on 2024-12-12 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('body_type', models.CharField(default=None, max_length=50)),
                ('fuel_type', models.CharField(default=None, max_length=2)),
                ('transmission_type', models.CharField(default=None, max_length=50)),
                ('variantcolor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master.variantcolor', unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
