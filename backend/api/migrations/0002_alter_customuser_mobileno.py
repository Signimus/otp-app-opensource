# Generated by Django 4.0.6 on 2022-07-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='mobileNo',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]