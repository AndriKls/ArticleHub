# Generated by Django 5.1.1 on 2024-12-12 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='word_column',
            new_name='word_count',
        ),
    ]
