# Generated by Django 5.0 on 2024-04-27 10:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurants', '0002_delete_dresscode_delete_hours_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DressCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant_Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('Menu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
            ],
        ),
    ]
