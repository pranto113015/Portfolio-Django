# Generated by Django 4.2.16 on 2024-09-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_testimonial_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(default='#', upload_to='static/assets/img/testimonials/'),
        ),
    ]
