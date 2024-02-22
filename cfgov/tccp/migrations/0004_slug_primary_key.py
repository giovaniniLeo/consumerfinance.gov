# Generated by Django 3.2.23 on 2024-02-22 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tccp", "0003_cardsurveydata_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cardsurveydata",
            name="id",
        ),
        migrations.AlterField(
            model_name="cardsurveydata",
            name="slug",
            field=models.SlugField(
                max_length=255, primary_key=True, serialize=False
            ),
        ),
    ]
