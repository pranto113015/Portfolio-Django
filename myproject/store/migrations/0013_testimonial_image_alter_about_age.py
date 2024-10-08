# Generated by Django 4.2.16 on 2024-09-10 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(blank='', default='#', null='', upload_to='static/assets/img/testimonials/'),
        ),
        migrations.AlterField(
            model_name='about',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]
