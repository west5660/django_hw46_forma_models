# Generated by Django 4.2.5 on 2023-09-04 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmodels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=15)),
                ('proizv', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('gn', models.CharField(max_length=15)),
            ],
        ),
    ]
