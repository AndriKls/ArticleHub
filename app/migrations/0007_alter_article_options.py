# Generated by Django 5.1.4 on 2024-12-15 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_article_content_alter_article_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
    ]
