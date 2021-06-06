# Generated by Django 3.2.4 on 2021-06-06 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_mutant_dna', models.IntegerField()),
                ('count_human_dna', models.IntegerField()),
                ('ratio', models.FloatField()),
            ],
        ),
    ]