# Generated by Django 4.0.6 on 2022-11-12 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crossroadsbe', '0010_plays_created'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Facts',
            new_name='Fact',
        ),
        migrations.RenameModel(
            old_name='Plays',
            new_name='Play',
        ),
    ]
