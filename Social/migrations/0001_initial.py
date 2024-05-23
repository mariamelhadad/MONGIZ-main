# Generated by Django 5.0.3 on 2024-05-22 19:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('User', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Husband_or_Wife_Name', models.CharField(default=None, max_length=200)),
                ('Sons_Name1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Sons_Name2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Sons_Name3', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Sons_Name4', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Sons_Number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='social_state',
            fields=[
                ('User', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Personel_Card', models.ImageField(upload_to='Social/social_state/Personel_Card/%y/%m/%d')),
                ('Marital_state', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], default='Single', max_length=10)),
                ('Phone_Number', models.CharField(default=None, max_length=11, unique=True)),
                ('Address', models.CharField(default=None, max_length=40)),
            ],
        ),
    ]
