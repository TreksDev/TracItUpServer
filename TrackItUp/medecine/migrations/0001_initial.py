# Generated by Django 5.0.3 on 2024-03-16 17:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AprovedMedecine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_prescription', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='UserMedecine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('exp_date', models.DateField()),
                ('is_shared', models.BooleanField(default=False)),
                ('shared_qty', models.IntegerField(default=1)),
                ('medecine', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medecine.aprovedmedecine')),
            ],
        ),
    ]
