# Generated by Django 4.2.16 on 2024-09-09 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_link', models.URLField(max_length=1000)),
                ('fb_link', models.URLField(max_length=1000)),
                ('i_link', models.URLField(max_length=1000)),
                ('in_link', models.URLField(max_length=1000)),
            ],
        ),
    ]
