# Generated by Django 3.0.6 on 2020-05-24 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(default='', max_length=200),
        ),
    ]
