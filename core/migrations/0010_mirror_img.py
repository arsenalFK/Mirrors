# Generated by Django 3.2.6 on 2021-08-24 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_another_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='mirror',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
