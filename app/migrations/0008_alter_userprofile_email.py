# Generated by Django 5.1.4 on 2024-12-15 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_article_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email address'),
        ),
    ]
