# Generated by Django 4.2.16 on 2024-09-09 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_social'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='fb_link',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='i_link',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='in_link',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='t_link',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
