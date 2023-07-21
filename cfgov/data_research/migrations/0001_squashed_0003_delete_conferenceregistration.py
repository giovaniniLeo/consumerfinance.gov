# Generated by Django 3.2.18 on 2023-04-25 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('v1', '0001_squashed_0235_add_use_json_field_to_streamfields'),
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fips', models.CharField(blank=True, db_index=True, max_length=6)),
                ('name', models.CharField(blank=True, max_length=128)),
                ('valid', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='MetroArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fips', models.CharField(blank=True, db_index=True, max_length=6)),
                ('name', models.CharField(blank=True, max_length=128)),
                ('counties', models.JSONField(blank=True, help_text='FIPS list of counties in the MSA')),
                ('states', models.JSONField(blank=True, help_text='FIPS list of states touched by MSA')),
                ('valid', models.BooleanField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MortgageDataConstant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(blank=True, help_text='OPTIONAL SLUG', max_length=255)),
                ('value', models.IntegerField(blank=True, null=True)),
                ('date_value', models.DateField(blank=True, help_text='CHOOSE THE LAST MONTH OF DATA TO DISPLAY (AND SELECT THE FIRST DAY OF THAT MONTH)', null=True)),
                ('note', models.TextField(blank=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MortgagePerformancePage',
            fields=[
                ('browsepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='v1.browsepage')),
            ],
            options={
                'abstract': False,
            },
            bases=('v1.browsepage',),
        ),
        migrations.CreateModel(
            name='MSAMortgageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fips', models.CharField(blank=True, db_index=True, max_length=6)),
                ('date', models.DateField(blank=True, db_index=True)),
                ('total', models.IntegerField(null=True)),
                ('current', models.IntegerField(null=True)),
                ('thirty', models.IntegerField(null=True)),
                ('sixty', models.IntegerField(null=True)),
                ('ninety', models.IntegerField(null=True)),
                ('other', models.IntegerField(null=True)),
                ('msa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data_research.metroarea')),
            ],
            options={
                'ordering': ['date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NationalMortgageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fips', models.CharField(blank=True, db_index=True, max_length=6)),
                ('date', models.DateField(blank=True, db_index=True)),
                ('total', models.IntegerField(null=True)),
                ('current', models.IntegerField(null=True)),
                ('thirty', models.IntegerField(null=True)),
                ('sixty', models.IntegerField(null=True)),
                ('ninety', models.IntegerField(null=True)),
                ('other', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ['date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fips', models.CharField(blank=True, db_index=True, max_length=2)),
                ('name', models.CharField(blank=True, db_index=True, max_length=128)),
                ('abbr', models.CharField(max_length=2)),
                ('ap_abbr', models.CharField(help_text="The AP Stylebook's state abbreviation", max_length=20)),
                ('counties', models.JSONField(blank=True, help_text='FIPS list of counties in the state')),
                ('non_msa_counties', models.JSONField(blank=True, help_text='FIPS list of counties in the state that are not in an MSA')),
                ('msas', models.JSONField(blank=True, help_text='FIPS list of MSAs in the state')),
                ('non_msa_valid', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='StateMortgageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fips', models.CharField(blank=True, db_index=True, max_length=6)),
                ('date', models.DateField(blank=True, db_index=True)),
                ('total', models.IntegerField(null=True)),
                ('current', models.IntegerField(null=True)),
                ('thirty', models.IntegerField(null=True)),
                ('sixty', models.IntegerField(null=True)),
                ('ninety', models.IntegerField(null=True)),
                ('other', models.IntegerField(null=True)),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data_research.state')),
            ],
            options={
                'ordering': ['date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NonMSAMortgageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fips', models.CharField(blank=True, db_index=True, max_length=6)),
                ('date', models.DateField(blank=True, db_index=True)),
                ('total', models.IntegerField(null=True)),
                ('current', models.IntegerField(null=True)),
                ('thirty', models.IntegerField(null=True)),
                ('sixty', models.IntegerField(null=True)),
                ('ninety', models.IntegerField(null=True)),
                ('other', models.IntegerField(null=True)),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data_research.state')),
            ],
            options={
                'ordering': ['date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CountyMortgageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fips', models.CharField(blank=True, db_index=True, max_length=6)),
                ('date', models.DateField(blank=True, db_index=True)),
                ('total', models.IntegerField(null=True)),
                ('current', models.IntegerField(null=True)),
                ('thirty', models.IntegerField(null=True)),
                ('sixty', models.IntegerField(null=True)),
                ('ninety', models.IntegerField(null=True)),
                ('other', models.IntegerField(null=True)),
                ('county', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data_research.county')),
            ],
            options={
                'ordering': ['date'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='county',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_research.state'),
        ),
        migrations.CreateModel(
            name='MortgageMetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('json_value', models.JSONField(blank=True, null=True)),
                ('note', models.TextField(blank=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Mortgage metadata',
            },
        ),
    ]
