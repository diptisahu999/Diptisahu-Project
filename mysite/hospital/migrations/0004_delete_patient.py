# Generated by Django 4.0.6 on 2022-11-10 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_patient'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
