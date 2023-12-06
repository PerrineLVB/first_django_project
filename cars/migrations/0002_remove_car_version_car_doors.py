# Generated by Django 5.0 on 2023-12-06 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='version',
        ),
        migrations.AddField(
            model_name='car',
            name='doors',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
