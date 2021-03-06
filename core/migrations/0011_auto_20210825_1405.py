# Generated by Django 3.2.6 on 2021-08-25 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_mirror_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='production',
            name='description',
        ),
        migrations.AddField(
            model_name='another',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mirror',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='production',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'MIRROR'), (2, 'ANOTHER')], default=0),
        ),
    ]
