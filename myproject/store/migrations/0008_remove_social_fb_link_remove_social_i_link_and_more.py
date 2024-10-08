# Generated by Django 4.2.16 on 2024-09-09 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_social_fb_link_alter_social_i_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='social',
            name='fb_link',
        ),
        migrations.RemoveField(
            model_name='social',
            name='i_link',
        ),
        migrations.RemoveField(
            model_name='social',
            name='in_link',
        ),
        migrations.RemoveField(
            model_name='social',
            name='t_link',
        ),
        migrations.AddField(
            model_name='social',
            name='link',
            field=models.URLField(default='01', max_length=100),
        ),
        migrations.AddField(
            model_name='social',
            name='social_icon',
            field=models.CharField(default='01', max_length=100),
        ),
    ]
