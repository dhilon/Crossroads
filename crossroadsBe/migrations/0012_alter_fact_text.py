# Generated by Django 4.0.6 on 2022-11-12 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crossroadsbe', '0011_rename_facts_fact_rename_plays_play'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fact',
            name='text',
            field=models.TextField(max_length=200),
        ),
    ]
