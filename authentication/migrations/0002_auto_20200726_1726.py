# Generated by Django 3.0.5 on 2020-07-26 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
    ]
