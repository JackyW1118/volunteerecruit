# Generated by Django 3.1 on 2020-10-05 20:16

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='firstname',
            field=models.CharField(max_length=100, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='lastname',
            field=models.CharField(max_length=100, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='message',
            field=models.TextField(blank=True, help_text='Message to the recruitor', null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31, null=True),
        ),
    ]