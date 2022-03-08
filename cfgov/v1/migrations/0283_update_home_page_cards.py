# Generated by Django 3.2.12 on 2022-03-08 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0282_home_page_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='card_heading',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='homepagecard',
            name='text',
            field=models.TextField(blank=True, help_text='100 characters maximum (including spaces).', max_length=100),
        ),
    ]
