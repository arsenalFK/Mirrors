# Generated by Django 3.2.6 on 2021-08-25 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210825_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mirror',
            name='type',
            field=models.CharField(choices=[('Разборное', 'Разборное'), ('Цельное', 'Цельное')], max_length=100),
        ),
        migrations.AlterField(
            model_name='production',
            name='type',
            field=models.CharField(choices=[('MIRROR', 'MIRROR'), ('ANOTHER', 'ANOTHER')], max_length=100),
        ),
    ]
