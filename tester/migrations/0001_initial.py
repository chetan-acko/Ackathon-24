# Generated by Django 3.2.18 on 2023-09-29 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigurableData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ackodrive_finance_slabs', models.JSONField(default=list)),
                ('value_propositions', models.JSONField(default=list)),
            ],
            options={
                'verbose_name': 'Configurable Data',
                'verbose_name_plural': 'Configurable Data',
            },
        ),
    ]