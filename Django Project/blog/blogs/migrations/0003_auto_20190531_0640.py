# Generated by Django 2.2.1 on 2019-05-31 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blogpost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='text',
            field=models.TextField(max_length=400),
        ),
    ]
