# Generated by Django 3.1 on 2020-09-07 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200906_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
