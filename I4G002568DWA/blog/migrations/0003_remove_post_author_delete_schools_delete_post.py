# Generated by Django 4.0.5 on 2022-06-18 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_schools'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Author',
        ),
        migrations.DeleteModel(
            name='Schools',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
