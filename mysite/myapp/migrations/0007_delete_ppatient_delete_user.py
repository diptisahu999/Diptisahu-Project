# Generated by Django 4.1.2 on 2022-11-09 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_ppatient'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PPatient',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]