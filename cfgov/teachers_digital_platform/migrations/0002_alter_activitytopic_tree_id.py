# Generated by Django 3.2.12 on 2022-03-15 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers_digital_platform', '0001_2022_squash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitytopic',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, editable=False),
        ),
    ]
