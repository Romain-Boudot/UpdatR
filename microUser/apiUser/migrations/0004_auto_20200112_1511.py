# Generated by Django 3.0.2 on 2020-01-12 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiUser', '0003_auto_20200112_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rapport',
            old_name='rapport',
            new_name='rapportInfo',
        ),
    ]
