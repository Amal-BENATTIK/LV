# Generated by Django 4.1 on 2023-05-05 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myappvoiture", "0004_voiture1_bl_voiture1_cl_voiture1_mp_voiture1_sunroof"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="client1",
            name="emai",
        ),
        migrations.AddField(
            model_name="client1",
            name="email",
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="client1",
            name="Pswd",
            field=models.CharField(max_length=255),
        ),
    ]
