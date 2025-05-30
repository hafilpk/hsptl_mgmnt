# Generated by Django 5.2 on 2025-04-25 23:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=100)),
                ('doc_image', models.ImageField(upload_to='doctors')),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.departments')),
            ],
        ),
    ]
