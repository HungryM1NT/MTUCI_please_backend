# Generated by Django 4.2.7 on 2023-11-18 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='first_level_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='appuser',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='appuser',
            name='second_level_score',
            field=models.IntegerField(default=0),
        ),
    ]
