# Generated by Django 4.2.16 on 2024-09-09 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_social_link_alter_social_social_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='link',
            field=models.URLField(max_length=1000),
        ),
    ]
