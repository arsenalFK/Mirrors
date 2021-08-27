# Generated by Django 3.2.6 on 2021-08-24 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210824_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('man_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='mirror',
            name='color',
        ),
        migrations.RemoveField(
            model_name='mirror',
            name='manufacture',
        ),
        migrations.AddField(
            model_name='mirror',
            name='color',
            field=models.ManyToManyField(null=True, to='core.Color'),
        ),
        migrations.AddField(
            model_name='mirror',
            name='manufacture',
            field=models.ManyToManyField(null=True, to='core.Manufacture'),
        ),
    ]
